import sqlite3
from utils.ai_service import generate_response

conn = sqlite3.connect("chat_history.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
user TEXT,
message TEXT
)
""")

def save_chat(user, message):

    cursor.execute(
        "INSERT INTO chats VALUES (?,?)",
        (user, message)
    )

    conn.commit()


def load_chats(user):

    cursor.execute(
        "SELECT message FROM chats WHERE user=?",
        (user,)
    )

    return cursor.fetchall()