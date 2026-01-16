import os
from dotenv import load_dotenv
from langchain_ollama.llms import OllamaLLm
from langchain_core.prmpts import ChatPromptTemplate

from prompts import research_report_prompt, analysis_report_prompt, linkedin_post_prompt
from schemas.article import ArticleSchema


load_dotenv()

model = OllamaLLM(model="llama3.2")

template = """
You are an expert research analyst. Given the following topic, generate a comprehensive research report that includes relevant data, statistics, and insights.
Topic: {theme}
"""

prompt = ChatPromptTemplate(template)

chain = prompt | model  # invoke chain

result = chain.invoke(theme="Artificial Intelligence in Healthcare")

print(result)

# research agent using Gemini API


class gemini_agent():
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_name = "gemini-1.5 flash"

    def research_theme(self, prompt: str, theme) -> str:
        # Placeholder for actual API call to Gemini model
        return f"Generated text for prompt: {prompt}"
