def recommend_topics(history, ask_ai):

    prompt = f"""
Based on this learning history recommend topics:

{history}

Give 5 topics.
"""

    return ask_ai(prompt)