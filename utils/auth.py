import streamlit as st
import sqlite3

# ---------------- DB ----------------

conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
)
""")
conn.commit()


# ---------------- SIGNUP ----------------

def signup(username, password):
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False


# ---------------- LOGIN ----------------

def login_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()


# ---------------- UI ----------------

def login():

    st.title("🔐 Login / Signup")

    menu = st.radio("Choose option", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if menu == "Signup":
        if st.button("Create Account"):
            if signup(username, password):
                st.success("✅ Account created! Please login")
            else:
                st.error("❌ Username already exists")

    else:
        if st.button("Login"):
            user = login_user(username, password)

            if user:
                st.session_state.user = username
                st.success("✅ Login successful")
                st.rerun()
            else:
                st.error("❌ Invalid credentials")