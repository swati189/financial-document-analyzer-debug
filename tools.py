import os
from dotenv import load_dotenv
load_dotenv()

import PyPDF2
from crewai_tools import tool


@tool
def financial_document_tool(path: str = "data/sample.pdf") -> str:
    """
    Tool to read and extract text from a financial PDF document.
    """

    text = ""

    try:
        with open(path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

        if text.strip() == "":
            return "No readable text found in the PDF."

        return text

    except Exception as e:
        return f"Error reading PDF file: {str(e)}"