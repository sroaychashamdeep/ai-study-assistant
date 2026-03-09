def summarize_notes(text, model):

    prompt = f"Summarize this for students:\n{text}"

    response = model.generate_content(prompt)

    return response.text