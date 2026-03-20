from google import genai
import os
import base64

# ---------------- CONFIG ----------------

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.1-flash-lite-preview"
# MODEL = "gemini-2.0-flash"   # fallback if needed


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


# ---------------- IMAGE ANALYSIS (FIXED) ----------------

def analyze_image(image_bytes, mime_type="image/jpeg"):
    try:
        encoded_image = base64.b64encode(image_bytes).decode("utf-8")

        response = client.models.generate_content(
            model=MODEL,
            contents=[
                {
                    "parts": [
                        {"text": "Analyze this image in detail."},
                        {
                            "inline_data": {
                                "mime_type": mime_type,
                                "data": encoded_image
                            }
                        }
                    ]
                }
            ]
        )

        return response.text if response.text else "⚠ No output from image."

    except Exception as e:
        return f"❌ Image Error: {str(e)}"