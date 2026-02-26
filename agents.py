# Import libraries
from crewai import Agent
from langchain_openai import ChatOpenAI
from tools import financial_document_tool

# Load LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3
)

# Create Financial Analyst Agent
financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial documents and provide accurate financial insights.",
    backstory=(
        "You are an experienced financial analyst skilled in analyzing "
        "financial statements, identifying risk factors, and providing "
        "investment recommendations based on data."
    ),
    verbose=True,
    tools=[financial_document_tool],
    llm=llm
)