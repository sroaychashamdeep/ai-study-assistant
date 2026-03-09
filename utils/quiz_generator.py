def generate_quiz(topic, model):

    prompt = f"""
    Create 5 multiple choice questions about {topic}.
    Include answers.
    """

    response = model.generate_content(prompt)

    return response.text