# 📄 PDF Assistant with Gemini

A simple AI-powered PDF summarizer using Google's Gemini model.

This app allows users to upload a PDF, extract the text, and use Gemini to summarize, extract key points, or answer questions about the document.



## 🚀 Features
- Upload a PDF
- Summarize its contents
- Extract key points
- Ask custom questions about the document



## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/doc-summarizer.git
cd your-repo-name
``` 

2. **Install dependencies**

Using Python version 3.10.



```bash
pip install -r requirements.txt
```

3. **🔑 Getting your Gemini API Key**

* Go to Google AI Studio: https://aistudio.google.com/apikey
* Sign in and create a new API key.
* Copy the API key.

4. **🛡️ Create your .env file**
In the project root directory, create a file named .env and add your API key:

```ini
GOOGLE_API_KEY=your-api-key-here
```

Make sure .env is NOT committed to GitHub!

## 🏃 Running the App
In the terminal, run:

```bash
streamlit run main.py
```

You should see the app open in your browser at http://localhost:8501.

## 📚 Brief Explanation

* Text Extraction: The app uses PyMuPDF to extract text from PDFs.

* Gemini API: The extracted text is sent to Google's Gemini model via the official google-generativeai Python library.

* Outputs: You can ask the model to summarize, list key points, or answer specific questions based on the uploaded document.

## 📦 Requirements

* Python 3.10+
* Streamlit
* PyMuPDF (fitz)
* google-generativeai
* python-dotenv
