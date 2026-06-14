import sqlite3

conn = sqlite3.connect(
    "database.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS packages(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_name TEXT,
tracking_id TEXT,
courier_company TEXT,
status TEXT
)
""")

conn.commit()