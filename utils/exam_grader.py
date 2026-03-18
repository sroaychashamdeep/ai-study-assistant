from utils.ai_service import ask_ai


def grade_answer(question, user_answer):

    if not question.strip() or not user_answer.strip():
        return "⚠ Please enter both question and answer."

    prompt = f"""
You are an AI exam evaluator.

Question:
{question}

Student Answer:
{user_answer}

Evaluate based on:
- Accuracy
- Completeness
- Clarity

Return:
Score (out of 10)
Feedback
Strengths
Weaknesses
Improvements
"""

    return ask_ai(prompt)