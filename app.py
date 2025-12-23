import streamlit as st
import zipfile
import os
import tempfile
import pandas as pd
import pymupdf
import dotenv

from dotenv import load_dotenv
from typing import TypedDict,Optional,Annotated
from docx import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gem")

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title(" AI-Powered Resume Analyzer & CSV Generator")
st.write("Upload a ZIP file containing multiple resumes (PDF or DOCX). "
        "The system will extract structured information and generate a CSV.")

zip_file = st.file_uploader("Upload ZIP file", type=["zip"])

def extract_text_from_pdf(path):
    doc = pymupdf.open(path)
    text = ""
    for page in doc:
        text = text+page.get_text()
    return text

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_resume_text(path):
    if path.endswith(".pdf"):
        return extract_text_from_pdf(path)
    elif path.endswith(".docx"):
        return extract_text_from_docx(path)
    return ""

class DataFormat(TypedDict):
    name: str
    email: str
    phone: str
    skills: str
    years_of_experience: int
    summary: str
    linkedin_or_github: str

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = llm.with_structured_output(DataFormat)

prompt = ChatPromptTemplate.from_template(
    """You are an AI Resume Analyzer.
    Extract structured information from the resume text below.
    If a field is missing, return "Not Available".

    Resume Text:
    {resume_text} """)

if zip_file and st.button("Analyze Resumes", type="primary"):

    with st.spinner("Analyzing resumes... Please wait"):
        temp_dir = tempfile.mkdtemp()

        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        extracted_results = []

        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.endswith((".pdf", ".docx")):
                    file_path = os.path.join(root, file)
                    resume_text = extract_resume_text(file_path)

                    if resume_text.strip():
                        formatted_prompt = prompt.format(
                        resume_text=resume_text[:4000])

                        parsed_output = parser.invoke(formatted_prompt)
                        parsed_output["resume_file"] = file

                        extracted_results.append(parsed_output)

        df = pd.DataFrame(extracted_results)
        st.session_state["resume_df"] = df

if "resume_df" in st.session_state:
    st.subheader(" Extracted Resume Data (Table Preview)")
    st.dataframe(st.session_state["resume_df"],use_container_width=True)

    csv_path = "resume_analysis.csv"
    st.session_state["resume_df"].to_csv(csv_path, index=False)

    with open(csv_path, "rb") as f:
        st.download_button(" Download CSV",
                            f,type="primary",
                            file_name="resume_analysis.csv",
                            mime="text/csv")
