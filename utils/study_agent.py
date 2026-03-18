def generate_study_kit(text, ask_ai):

    summary = ask_ai(
        f"Summarize the following study material:\n{text[:4000]}"
    )

    notes = ask_ai(
        f"Create structured study notes:\n{text[:4000]}"
    )

    flashcards = ask_ai(
        f"Create 10 flashcards from this text:\n{text[:4000]}"
    )

    quiz = ask_ai(
        f"Create 10 MCQ questions:\n{text[:4000]}"
    )

    exam = ask_ai(
        f"""
Create exam questions:

5 short questions
3 long questions

{text[:4000]}
"""
    )

    plan = ask_ai(
        f"""
Create a study plan based on this material.

{text[:4000]}
"""
    )

    return {
        "summary": summary,
        "notes": notes,
        "flashcards": flashcards,
        "quiz": quiz,
        "exam": exam,
        "plan": plan
    }