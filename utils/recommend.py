def recommend(history, ask_ai):

    prompt = f"""
Based on this study history recommend next topics:

{history}

Return 5 recommendations.
"""

    return ask_ai(prompt)