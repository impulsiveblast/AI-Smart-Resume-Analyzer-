# 📄 AI Smart Resume Analyzer

An AI-powered resume analysis application built with **Python, Streamlit, LangChain, and Google Gemini**. Upload your resume in PDF format and receive an AI-generated assessment covering your professional summary, key skills, improvement suggestions, and an overall resume score.

🔗 **Live Demo:** [Try AI Smart Resume Analyzer](https://nvjdydy6kmpb9hccfmnoun.streamlit.app/)

---

## ✨ Features

- **PDF Resume Upload:** Upload resumes in PDF format through an interactive interface.
- **Resume Text Extraction:** Extracts text from uploaded PDF documents using LangChain's PyPDFLoader.
- **AI-Powered Resume Analysis:** Uses Google's Gemini Flash model to analyze resume content.
- **Key Skills Assessment:** Identifies important technical and professional skills mentioned in the resume.
- **Improvement Suggestions:** Provides actionable recommendations to improve resume quality and presentation.
- **Resume Scoring:** Generates an overall score out of 100 across four evaluation categories:
  - Skills Match – 30 points
  - Experience & Achievements – 30 points
  - Clarity & Formatting – 20 points
  - Overall Impression – 20 points
- **Interactive Interface:** Displays extracted resume text and AI-generated analysis side by side.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| LangChain | LLM integration and document loading |
| Google Gemini API | AI-powered resume analysis |
| PyPDFLoader | PDF text extraction |
| python-dotenv | Local environment variable management |

## ⚙️ How It Works

1. The user uploads a resume in PDF format.
2. The application temporarily saves the uploaded PDF.
3. PyPDFLoader extracts text from the document.
4. The extracted text is displayed in the resume preview.
5. LangChain sends the resume content to Google's Gemini model along with a structured analysis prompt.
6. Gemini evaluates the resume and generates a summary, skills assessment, improvement suggestions, and category-wise scores.
7. The results are displayed in the Streamlit interface.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/impulsiveblast/AI-Smart-Resume-Analyzer-.git
```

### 2. Navigate to the project directory

```bash
cd AI-Smart-Resume-Analyzer-
```

### 3. Create a virtual environment

```bash
python -m venv env
```

Activate it:

**Windows**
```bash
env\Scripts\activate
```

**macOS / Linux**
```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure your Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 6. Run the application

```bash
streamlit run main.py
```

The application will open locally in your browser.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key used to access Google's Gemini models |

**Security:** Never commit your `.env` file or expose your API key in public repositories. For Streamlit Community Cloud, configure the key through the application's Secrets settings.

## 📁 Project Structure

```text
AI-Smart-Resume-Analyzer/
│
├── main.py             # Streamlit application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore          # Excluded files and secrets
```

## 🔮 Future Improvements

- Job-description-based resume matching.
- ATS compatibility assessment.
- Structured JSON output for resume evaluation.
- Downloadable resume analysis reports.
- Support for additional document formats.
- More detailed feedback on project descriptions and professional achievements.

## ⚠️ Disclaimer

The generated scores and recommendations are AI-generated assessments and should be treated as guidance rather than definitive hiring or ATS evaluations. Avoid uploading confidential personal information unless you are comfortable sharing it with the AI service.

---

**Built with Python, Streamlit, LangChain, and Google Gemini.**
