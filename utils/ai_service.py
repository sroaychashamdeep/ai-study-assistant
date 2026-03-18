from google import genai
import os

# ---------------- CONFIG ----------------

# Load API key from Streamlit secrets or environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Use latest model (fallback if needed)
MODEL = "gemini-3.1-flash-lite-preview"
# MODEL = "gemini-2.0-flash"   # ← use this if 3.1 fails


# ---------------- MAIN RESPONSE ----------------

def generate_response(prompt):
    """
    Generate a normal AI response
    Used in: Study Agent, Exam Grader, Course Builder
    """
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
    """
    Stream response (Chat page)
    """
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
    """
    Universal AI function (used across app)
    """
    return generate_response(prompt)


# ---------------- OPTIONAL: SMART RESPONSE (ADVANCED) ----------------

def ask_ai_with_context(prompt, context=""):
    """
    Use context-aware AI (for memory / RAG)
    """
    full_prompt = f"""
Context:
{context}

User:
{prompt}
"""
    return generate_response(full_prompt)