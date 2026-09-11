import json
from datetime import datetime

try:
    with open("expence_tracker.json", "r") as file:
        tracker = json.load(file)
except FileNotFoundError:
    tracker = []

def save_file():
    with open("expence_tracker.json", "w") as file:
        json.dump(tracker, file, indent=4)

def is_int(num):
    try:
        return int(num) > 0
    except ValueError:
        print("Invalid input!")
        return False

def is_float(num):
    try:
        return float(num) > 0
    except ValueError:
        print("Invalid input!")
        return False

def show_menu():
    print("""
    1. Add an expense
    2. Update an expense
    3. Delete an expense
    4. View all expenses
    5. View summary of all expenses
    6. View summary of all expenses for a specific month
    7. Exit
    """)

def now():
    return datetime.now()

def show_expenses(expenses):
    for expense in expenses:
        print(f"""ID: {expense['ID']} | Description: {expense['Description']} | Amount: {expense['Amount']} | Created at: {expense['Created at']} | Updated at: {expense['Updated at']}""")

while True:
    show_menu()
    action = input("Choose the action: ")
    if is_int(action):
        action = int(action)
        if action == 1:
            max_id = 0
            for i in tracker:
                if max_id < i.get("ID"):
                    max_id = i.get("ID")
            desc = input("Description: ")
            amount = input("Amount: ")
            if is_float(amount):
                amount = float(amount)
                purchase = {
                    "ID": max_id + 1,
                    "Description": desc,
                    "Amount": amount,
                    "Created at": str(now()),
                    "Updated at": str(now())
                }
                tracker.append(purchase)
                save_file()

        elif action == 2:
            show_expenses(tracker)
            update = input("Choose the purchase: ")
            if is_int(update):
                flag = False
                update = int(update)
                for purchase in tracker:
                    if purchase["ID"] == update:
                        flag = True
                        crtd_at = purchase["Created at"]
                        descript = input("Description: ")
                        amo = input("Amount: ")
                        if is_float(amo):
                            amo = float(amo)
                            this_purchase = {
                                "ID": update,
                                "Description": descript,
                                "Amount": amo,
                                "Created at": crtd_at,
                                "Updated at": str(now())
                            }
                            for index, purchase in enumerate(tracker):
                                if purchase["ID"] == update:
                                    tracker[index] = this_purchase
                            save_file()
                            break
                        elif not flag:
                            print("No such purchase!")
                            break

        elif action == 3:
            show_expenses(tracker)
            delete = input("Choose an expense to delete: ")
            if is_int(delete):
                delete = int(delete)
                for index, expense in enumerate(tracker):
                    this_id_del = expense["ID"]
                    if this_id_del == delete:
                        del tracker[index]
                        break
                save_file()

        elif action == 4:
            show_expenses(tracker)

        elif action == 5:
            summ = 0
            for expense in tracker:
                summ += float(expense["Amount"])
            print(f"The summary of all expenses: {summ}")

        elif action == 6:
            summ_month = 0
            month = input("Choose a month (with numbers): ")
            if is_int(month):
                month = int(month)
                for expense in tracker:
                    if int(expense["Created at"][5:7]) == month:
                        summ_month += float(expense["Amount"])
            print(summ_month)

        elif action == 7:
            break
        else:
            print("No such command!")