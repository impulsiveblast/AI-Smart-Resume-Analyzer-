from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)
from langchain_core.vectorstores import InMemoryVectorStore
from time import sleep
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
# 1. Load PDF
import tempfile

load_dotenv()



st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
st.title("📄 Resume Analyzer")
st.markdown("""Upload your resume in PDF format, and our AI will analyze it to provide you with a comprehensive assessment. This includes **your resume analysis, key skills assessment, and improvement suggestions**.
""")


uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

txt=""
if uploaded_file:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file_path = temp_file.name

        file = PyPDFLoader(temp_file_path)
        pdf = file.load()

        txt = ""
        for page in pdf:
            txt += page.page_content + "\n\n"

    except Exception as e:
        st.error(f"Error loading PDF: {e}")

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    for page in pdf:
      text=page.page_content
      txt+=text+"\n\n"


col1, col2 = st.columns([1, 1])


with col1:
    st.subheader("Resume Preview")
    st.text_area("Resume Text", value=txt, height=400)

with col2:
    st.subheader("AI Analysis")

    if st.button("Analyze Resume"):  # Button to trigger analysis
        with st.spinner("Analyzing resume..."):  # Loading indicator

            prompt = f"""
            You are a resume expert.
            Analyze the following resume and provide:
            1. Summary
            2. List of key skills
            3. Suggestions for improvement
            4. A score out of 100 based on:
                - Skills match (30 points)
                - Experience & achievements (30 points)
                - Clarity & formatting (20 points)
                - Overall impression (20 points)

            Also provide the individual category scores in JSON.

            Resume:
            {txt}
            """
            
            # Initialize the Google Generative AI model
            
            llm=ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
             # google_api_key=GOOGLE_API_KEY,
            max_retries=6,
            max_delay=60,


            )
            # Generate the analysis
            response = llm.invoke([prompt])
            analysis = response.content

            if isinstance(analysis, list):
                analysis = "".join(
                    item.get("text", "") if isinstance(item, dict) else str(item)
                    for item in analysis
                )

            analysis = analysis.strip()

            st.text_area("AI Analysis Result", value=analysis, height=400)


             



