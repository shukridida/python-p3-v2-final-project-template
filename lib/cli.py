
from helpers import (
    add_user,
    list_users,
    delete_user,
    add_transaction,
    list_transactions,
    delete_transaction,
    add_category,
    list_categories,
    delete_category
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit()
        elif choice == "1":
            register_user()
        elif choice == "2":
            list_users_func()
        elif choice == "3":
            add_new_transaction()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            delete_existing_transaction()
        elif choice == "6":
            add_new_category()
        elif choice == "7":
            view_categories()
        elif choice == "8":
            delete_existing_category()
        elif choice == "9":
            exit()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("1. Register a new user")
    print("2. List all users")
    print("3. Add a new transaction")
    print("5. Delete a transaction")
    print("6. Add a new category")
    print("7. List all categories")
    print("8. Delete a category")
    print("9. Exit the program")

def register_user():
    username = input("Enter new username: ")
    if username.strip():
        add_user(username)
        print(f"User '{username}' registered.")
    else:
        print("Username cannot be empty.")

def list_users_func():
    users = list_users()
    if users:
        print("List of registered users:")
        for user in users:
            print(f"ID: {user[0]}, Username: {user[1]}")
    else:
        print("No users registered.")

def add_new_transaction():
    user_id = int(input("Enter user ID: "))  
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        print("Available categories:")
        categories = list_categories()
        for category in categories:
            print(f"{category[0]}. {category[1]}")
        category_id = int(input("Enter category ID: "))
        account_id = int(input("Enter account ID: "))
        add_transaction(amount, description, category_id, user_id, account_id)
        print(f"Transaction of {amount} added.")
    except ValueError:
        print("Invalid input. Please enter the correct values.")

def view_transactions():
    user_id = int(input("Enter user ID: "))  # Dynamically input user ID
    transactions = list_transactions(user_id)
    if transactions:
        print("List of transactions:")
        for transaction in transactions:
            print(f"ID: {transaction[0]}, Amount: {transaction[1]}, Description: {transaction[2]}, Category: {transaction[3]}, Account: {transaction[4]}")
    else:
        print("No transactions found.")

def delete_existing_transaction():
    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
        delete_transaction(transaction_id)
        print(f"Transaction ID {transaction_id} deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid transaction ID.")

def add_new_category():
    name = input("Enter new category name: ")
    if name.strip():
        add_category(name)
        print(f"Category '{name}' added.")
    else:
        print("Category name cannot be empty.")

def view_categories():
    categories = list_categories()
    if categories:
        print("List of categories:")
        for category in categories:
            print(f"ID: {category[0]}, Name: {category[1]}")
    else:
        print("No categories found.")

def delete_existing_category():
    try:
        category_id = int(input("Enter category ID to delete: "))
        delete_category(category_id)
        print(f"Category ID {category_id} deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid category ID.")

if __name__ == "__main__":
    main()
