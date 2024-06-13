import sqlite3

def connect_db():
    return sqlite3.connect('users.db')

# Users CRUD operations
def add_user(username):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def update_user(user_id, new_username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, user_id))
    conn.commit()
    conn.close()

def list_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

# Categories CRUD operations
def add_category(name):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Category '{name}' already exists.")
    finally:
        conn.close()

def list_categories():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    conn.close()
    return categories

def delete_category(category_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
    conn.commit()
    conn.close()

# Transactions CRUD operations
def add_transaction(amount, description, category_id, user_id, account_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (amount, description, category_id, user_id, account_id)
        VALUES (?, ?, ?, ?, ?)
    """, (amount, description, category_id, user_id, account_id))
    conn.commit()
    conn.close()

def list_transactions(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.id, t.amount, t.description, c.name, a.name
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        JOIN accounts a ON t.account_id = a.id
        WHERE t.user_id = ?
    """, (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def delete_transaction(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
