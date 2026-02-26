## Importing libraries
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM


# ✅ Initialize LLM
llm = LLM(
    model="gpt-4o-mini",
    temperature=0.3  # lower = more factual, less hallucination
)


# ✅ Single Professional Financial Analyst Agent
financial_analyst = Agent(
    role="Senior Financial Analyst",

    goal="""
    Provide professional, data-driven financial analysis 
    strictly based on the provided financial document.
    """,

    backstory="""
    You are an experienced financial analyst with expertise in 
    corporate financial reporting, investment analysis, and risk evaluation.

    You carefully review financial statements, extract key metrics,
    identify trends, and provide evidence-based investment insights.

    You NEVER fabricate data.
    You NEVER invent financial numbers.
    You only analyze what is explicitly present in the document.
    """,

    verbose=True,
    memory=False,
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)