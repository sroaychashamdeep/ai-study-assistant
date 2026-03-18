import streamlit as st

def login():

    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin":

            st.session_state.user = username
            st.success("Login successful")
            st.rerun()

        else:
            st.error("Invalid credentials")