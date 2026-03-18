import streamlit as st
from utils.exam_grader import grade_answer

st.title("🧪 AI Exam Grader")

question = st.text_area("Enter Question")
answer = st.text_area("Your Answer")

if st.button("Evaluate"):
    result = grade_answer(question, answer)
    st.write(result)