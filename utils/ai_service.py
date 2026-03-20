from google import genai
import os

# ---------------- CONFIG ----------------

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# Use latest model (fallback if needed)
MODEL = "gemini-3.1-flash-lite-preview"
# MODEL = "gemini-2.0-flash"   # ← use if preview fails


# ---------------- NORMAL RESPONSE ----------------

def generate_response(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config={
                "temperature": 0.7,
                "max_output_tokens": 500
            }
        )
        return response.text if response.text else "⚠ No response generated."
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ---------------- STREAMING RESPONSE ----------------

def stream_response(prompt):
    try:
        response = client.models.generate_content_stream(
            model=MODEL,
            contents=prompt
        )

        for chunk in response:
            if chunk.text:
                yield chunk.text

    except Exception as e:
        yield f"❌ Error: {str(e)}"


# ---------------- UNIVERSAL FUNCTION ----------------

def ask_ai(prompt):
    return generate_response(prompt)


# ---------------- CONTEXT-AWARE (RAG / MEMORY) ----------------

def ask_ai_with_context(prompt, context=""):
    full_prompt = f"""
Context:
{context}

User:
{prompt}
"""
    return generate_response(full_prompt)


# ---------------- IMAGE ANALYSIS (VISION AI) ----------------

def analyze_image(image_bytes):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=[
                {"text": "Analyze this image in detail."},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": image_bytes
                    }
                }
            ]
        )

        return response.text if response.text else "⚠ No output from image analysis."

    except Exception as e:
        return f"❌ Image Error: {str(e)}"