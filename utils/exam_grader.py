from utils.ai_service import generate_response

def grade_answer(question, user_answer):

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

    Return in this format:

    Score: (out of 10)
    Feedback:
    Strengths:
    Weaknesses:
    Improvements:
    """

    result = generate_response(prompt)
    return result