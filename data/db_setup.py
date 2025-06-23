import sqlite3

def create_tables():
    conn = sqlite3.connect('coreboost.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        workout_name TEXT,
        date TEXT,
        duration INTEGER,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS diets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        meal_name TEXT,
        date TEXT,
        calories INTEGER,
        notes TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        reminder_time TEXT,
        reminder_type TEXT,
        active INTEGER DEFAULT 1,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database tables created successfully.")

# Optional: run this file directly to initialize
if __name__ == '__main__':
    create_tables()
