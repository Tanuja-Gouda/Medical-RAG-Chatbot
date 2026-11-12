import os

from google.genai import types
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    import streamlit as st
    api_key = st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_answer(question, context):

    prompt = f"""
    You are a medical information assistant.

    Answer the user's question using only the
    medical information provided below.

    If the answer is not available in the context,
    clearly say that the provided documents
    do not contain enough information.

    Do not diagnose diseases or prescribe medicines.

    Medical Context:
    {context}

    User Question:
    {question}

    Answer:
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
         config=types.GenerateContentConfig(
        temperature=1.0
    )
    )

    return response.text