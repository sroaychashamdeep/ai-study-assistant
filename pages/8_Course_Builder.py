import streamlit as st
from utils.course import generate_course

# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="Course Builder", page_icon="📚")

st.title("📚 AI Course Builder")

st.markdown("Generate a complete learning roadmap for any topic using AI.")

# ---------------- INPUT ----------------

topic = st.text_input("📌 Enter Topic (e.g. Machine Learning)")

level = st.selectbox(
    "🎯 Select Level",
    ["Beginner", "Intermediate", "Advanced"]
)

duration = st.selectbox(
    "⏳ Course Duration",
    ["2 Weeks", "1 Month", "3 Months"]
)

# ---------------- BUTTON ----------------

if st.button("Generate Course"):

    if not topic.strip():
        st.warning("⚠ Please enter a topic")
    
    else:
        with st.spinner("🤖 Creating your course..."):
            course = generate_course(topic, level, duration)

        # ---------------- OUTPUT ----------------

        st.success("✅ Course Generated")

        st.markdown("### 📘 Course Plan")
        st.write(course)