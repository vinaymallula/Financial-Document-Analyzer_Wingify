from crewai import Task
from agents import financial_analyst

analyze_financial_document = Task(
    description="""
You are a financial analyst.

Analyze the following financial document:

{document_text}

User Query:
{query}

IMPORTANT:
- Your response MUST be valid JSON
- Do NOT include markdown
- Do NOT include explanations outside JSON
""",

    expected_output="""
Return ONLY valid JSON in the following format:

{
  "executive_summary": "string",
  "financial_highlights": [
    "highlight 1",
    "highlight 2"
  ],
  "risk_analysis": [
    "risk 1",
    "risk 2"
  ],
  "investment_recommendation": "string"
}
""",

    agent=financial_analyst,
    async_execution=False,
)