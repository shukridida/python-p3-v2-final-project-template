import sqlite3

def create_tables():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    )
    ''')

    # Create categories table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')

    # Create accounts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')

    # Create transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        description TEXT,
        category_id INTEGER,
        user_id INTEGER,
        account_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id),
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (account_id) REFERENCES accounts (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
