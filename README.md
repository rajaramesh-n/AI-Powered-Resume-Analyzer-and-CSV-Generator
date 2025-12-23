# AI-Powered-Resume-Analyzer-and-CSV-Generator

• An AI-powered resume analysis application that automates the extraction of structured candidate information from bulk resumes.
The system accepts a ZIP file containing multiple PDF and DOCX resumes, analyzes them using LLMs, and generates a clean, structured CSV file for HR and recruitment workflows.

• This project is built with Streamlit, LangChain, and Gemini / OpenAI LLMs, following modern, production-ready practices.

**🚀 Project Overview**

• Recruiters and HR teams often receive resumes in bulk, typically as compressed ZIP files.
Manually reviewing resumes and extracting key information is time-consuming, repetitive, and error-prone.

This project solves that problem by:

• Automatically reading resumes

• Extracting structured information using LLMs

• Presenting results in a preview UI

• Generating a downloadable CSV for further analysis or ATS usage

**✨ Key Features**

📂 **Bulk Resume Upload**

• Accepts a ZIP file containing multiple resumes

• Supports PDF and DOCX formats

📄 **Automated Resume Text Extraction**

• Uses PyMuPDF (pymupdf) for PDFs

• Uses python-docx for Word documents

🧠 **LLM-Based Structured Data Extraction**

• Powered by Gemini (ChatGoogleGenerativeAI) or OpenAI

• Enforces a fixed schema using TypedDict-based structured output

• Avoids fragile prompt parsing

🖥️ **Interactive Streamlit UI**

• Preview extracted resume data in a tabular format

• Clean, simple, and user-friendly interface

📊 **CSV Generation & Download**

• One-click CSV export

• Ready for HR analytics, filtering, or ATS pipelines

⚙️ **Modern LangChain Architecture**

• No deprecated pipelines

• Uses native structured output for reliability

🧾 **Extracted Resume Fields**

The system extracts the following structured information:

• Name

• Email

• Phone Number

• Skills

• Years of Experience

• Professional Summary

• LinkedIn / GitHub Profile

**🏗️ Tech Stack**

| **Component**        | **Technology**       |
| ---------------- | ----------------- |
| Frontend         | Streamlit         |
| LLM              | Gemini / OpenAI   |
| AI Orchestration | LangChain         |
| PDF Parsing      | PyMuPDF (pymupdf) |
| DOCX Parsing     | python-docx       |
| Data Handling    | Pandas            |
| Output Format    | CSV               |


**📁 Project Structure**

AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/

**⚙️ Installation**

• pip install streamlit pandas pymupdf python-docx langchain langchain-core langchain-google-genai langchain-openai

**🔑 Environment Variables**

**Gemini (Recommended)**

• GOOGLE_API_KEY=your_gemini_api_key

**OpenAI (Optional)**

• OPENAI_API_KEY=your_openai_api_key

**▶️ Run the Application**

• streamlit run app.py

**🧪 How It Works**

• User uploads a ZIP file containing resumes

• The app extracts text from each PDF/DOCX

• Resume text is sent to the LLM with a fixed schema

• Structured data is returned as a Python dictionary

• Results are displayed in a preview UI

• User downloads the CSV file

**🎯 Use Cases**

• HR resume screening

• ATS preprocessing

• Bulk resume analysis

• Skill extraction & filtering

• AI portfolio projects

**📈 Learning Outcomes**

This project demonstrates:

• Real-world LLM-based information extraction

• Using TypedDict structured output with LangChain

• Building deployment-ready Streamlit applications

• Handling unstructured documents at scale

• Applying AI to HR and recruitment workflows
















