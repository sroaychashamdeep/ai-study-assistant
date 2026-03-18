from utils.ai_service import ask_ai


def generate_course(topic, level, duration):

    prompt = f"""
Create a complete course for learning {topic}.

Level: {level}
Duration: {duration}

Include:

1. Course Title
2. Learning Objectives
3. Weekly Plan (modules with topics)
4. Practical Projects
5. Recommended tools/resources

Format nicely with headings.
"""

    return ask_ai(prompt)