import time
import sqlite3
from datetime import datetime

def check_reminders():
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('coreboost.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, reminder_type FROM reminders
            WHERE reminder_time = ? AND active = 1
        ''', (now,))
        results = cursor.fetchall()

        for reminder in results:
            print(f"[Reminder 🔔] Time for your {reminder[1]}!")
            cursor.execute('UPDATE reminders SET active = 0 WHERE id = ?', (reminder[0],))

        conn.commit()
        conn.close()
        time.sleep(60)  # check every minute

# Optional: run for testing
if __name__ == '__main__':
    check_reminders()
