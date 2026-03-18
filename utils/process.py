import sqlite3

conn = sqlite3.connect("progress.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS progress(
user TEXT,
activity TEXT
)
""")

def save_progress(user,activity):

    cursor.execute(
        "INSERT INTO progress VALUES (?,?)",
        (user,activity)
    )

    conn.commit()