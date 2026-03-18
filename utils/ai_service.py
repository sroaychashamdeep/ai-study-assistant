from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ REQUIRED FUNCTION (THIS WAS MISSING)
def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text


# ✅ STREAMING
def stream_response(prompt):
    response = client.models.generate_content_stream(
        model="gemini-2.0-flash",
        contents=prompt
    )

    for chunk in response:
        if chunk.text:
            yield chunk.text