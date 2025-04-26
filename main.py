import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Config
genai.configure(api_key=api_key)  # or load from dotenv

# Load Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Extract text from PDF using PyMuPDF
def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# App UI
st.title("📄 PDF Assistant with Gemini")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")
    text = extract_text_from_pdf(uploaded_file)
    st.write("📃 Extracted Text Sample:")
    st.text(text[:1000])  # show a snippet

    task = st.selectbox("What would you like Gemini to do?", ["Summarize", "Extract key points", "Answer questions"])

    if task == "Answer questions":
        question = st.text_input("Ask a question about the document:")
        if st.button("Ask"):
            response = model.generate_content(f"Based on the following document:\n{text}\n\nAnswer the question:\n{question}")
            st.markdown("**💬 Answer:**")
            st.write(response.text)

    elif st.button("Run"):
        prompt = {
            "Summarize": f"Summarize the following document:\n\n{text}",
            "Extract key points": f"List the key points from this document:\n\n{text}"
        }[task]

        response = model.generate_content(prompt)
        st.markdown("**🧠 Gemini Response:**")
        st.write(response.text)
