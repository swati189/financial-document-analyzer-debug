from crewai import Task
from agents import financial_analyst
from tools import financial_document_tool


analyze_financial_task = Task(
    description=(
        "Analyze the uploaded financial document and provide:\n"
        "- Financial summary\n"
        "- Revenue and profit insights\n"
        "- Risk factors\n"
        "- Growth indicators\n"
        "- Investment recommendations"
    ),

    expected_output=(
        "A detailed financial analysis report with key insights "
        "and investment recommendations."
    ),

    agent=financial_analyst,
    tools=[financial_document_tool],
    async_execution=False
)