from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document
from tools1 import read_pdf

app = FastAPI(title="Financial Document Analyzer")


# -----------------------------
# Run CrewAI
# -----------------------------
def run_crew(query: str, file_path: str, document_text: str):
    """
    Run the CrewAI pipeline with document context
    """

    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential,
    )

    result = crew.kickoff(
        inputs={
            "query": query,
            "file_path": file_path,
            "document_text": document_text
        }
    )

    return result


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
async def root():
    return {"message": "Financial Document Analyzer API is running"}


# -----------------------------
# Analyze Endpoint
# -----------------------------
@app.post("/analyze")
async def analyze_financial_document_api(
    file: UploadFile = File(...),
    query: str = Form("Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        # Ensure folder exists
        os.makedirs("data", exist_ok=True)

        # Save uploaded file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text from PDF
        document_text = read_pdf(file_path)

        if not document_text.strip():
            raise HTTPException(status_code=400, detail="Uploaded PDF is empty or unreadable")

        # Run CrewAI
        response = run_crew(
            query=query.strip(),
            file_path=file_path,
            document_text=document_text
        )

        return {
            "status": "success",
            "query": query,
            "analysis": str(response),
            "file_processed": file.filename
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing financial document: {str(e)}"
        )

    finally:
        # Cleanup file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass


# -----------------------------
# Local Run
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)