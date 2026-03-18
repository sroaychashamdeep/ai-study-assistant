import streamlit as st
from utils.exam_grader import grade_answer

# ---------------- PAGE CONFIG ----------------

st.set_page_config(page_title="Exam Grader", page_icon="🧪")

st.title("🧪 AI Exam Grader")

st.markdown("Enter a question and your answer. The AI will evaluate it.")

# ---------------- INPUT ----------------

question = st.text_area("📌 Enter Question", height=150)
answer = st.text_area("✍️ Your Answer", height=150)

# ---------------- BUTTON ----------------

if st.button("Evaluate Answer"):

    if not question.strip() or not answer.strip():
        st.warning("⚠ Please enter both question and answer")
    
    else:
        with st.spinner("🤖 Evaluating your answer..."):
            result = grade_answer(question, answer)

        # ---------------- OUTPUT ----------------

        st.success("✅ Evaluation Complete")

        st.markdown("### 📊 Result")
        st.write(result)