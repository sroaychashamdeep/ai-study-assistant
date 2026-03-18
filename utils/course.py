from utils.ai_service import generate_response

def generate_course(topic, level="beginner"):

    prompt = f"""
    Create a structured course for learning {topic} at {level} level.

    Include:
    - Course title
    - Duration
    - Modules (with topics)
    - Learning outcomes
    - Project ideas

    Format nicely.
    """

    return generate_response(prompt)