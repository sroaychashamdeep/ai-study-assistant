import streamlit as st
from utils.course import generate_course

st.title("📚 AI Course Generator")

topic = st.text_input("Enter topic (e.g. Machine Learning)")
level = st.selectbox("Level", ["beginner", "intermediate", "advanced"])

if st.button("Generate Course"):
    course = generate_course(topic, level)
    st.write(course)