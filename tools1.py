## Importing libraries
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool
from PyPDF2 import PdfReader


from PyPDF2 import PdfReader

def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    
    return text