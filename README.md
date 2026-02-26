# Financial Document Analyzer - Debug Challenge (CrewAI)

# Project Overview
This project is a Financial Document Analyzer built using FastAPI and CrewAI. The system accepts financial PDF documents such as quarterly reports, extracts their content, and uses a Generative AI agent to produce structured financial analysis and investment insights.

Assignment Objective
The original repository contained multiple deterministic bugs that prevented execution and inefficient prompts that caused hallucinated or irrelevant outputs.

The goal of this assignment was to debug and fix the system, make the application fully functional, and improve prompts to ensure document-aware and meaningful analysis.

Bugs Identified and Fixes Applied

Incorrect CrewAI kickoff usage
Issue:
Inputs were passed incorrectly to the kickoff method, leading to runtime failures.

Fix:
Updated CrewAI kickoff usage to pass inputs using the inputs dictionary parameter, ensuring proper variable injection into tasks.

Broken tool imports (crewai_tools dependency)
Issue:
The original project relied on crewai_tools, which caused Windows C++ build and chromadb dependency errors.

Fix:
Removed crewai_tools completely and replaced it with a custom lightweight PDF utility implemented in tools1.py.

FastAPI multipart/form-data error
Issue:
The application crashed when uploading files because python-multipart was missing.

Fix:
Installed and configured python-multipart properly to handle file uploads.

PDF content not passed to the agent
Issue:
The LLM was not receiving the actual PDF content, resulting in generic or hallucinated responses.

Fix:
Extracted text from the uploaded PDF using a read_pdf function and passed the extracted document_text explicitly into CrewAI inputs.

Infinite reload and server looping
Issue:
Incorrect uvicorn reload configuration caused the server to restart continuously.

Fix:
Corrected the uvicorn startup configuration and ensured proper entry point usage.

Environment variable and API key errors
Issue:
Missing OpenAI API key caused authentication and rate limit errors.

Fix:
Configured environment variable loading using dotenv and ensured OPENAI_API_KEY is read correctly from the .env file.

# Tech Stack

Backend: FastAPI,
AI Orchestration: CrewAI,
LLM Provider: OpenAI via LiteLLM,
PDF Processing: PyPDF,
Programming Language: Python 3.10+.

# Setup Instructions

Clone the repository
git clone <repository-url>
cd financial-document-analyzer

Create and activate virtual environment
python -m venv venv
Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Configure environment variables
Create a .env file with the following content:
OPENAI_API_KEY=your_api_key_here

Run the application
uvicorn main:app --reload

Open the browser at:
http://127.0.0.1:8000/docs

# Final Result

The application is fully functional and stable.
It correctly processes uploaded PDFs, extracts text, performs document-aware AI analysis using CrewAI, and returns structured insights via a REST API.
