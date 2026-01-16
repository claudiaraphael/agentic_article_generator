import os
from dotenv import load_dotenv
from transformers import pipeline



from prompts import research_report_prompt, analysis_report_prompt, linkedin_post_prompt
from schemas.article import ArticleSchema


load_dotenv()

gemini_agent = pipeline(
    "text-generation",
    model="gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    device=0 # Use GPU (0 refers to the first GPU)
)

output = gemini_agent("How to get started with langchain?")
print(output)

# research agent using Gemini API
class researcher_agent():
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_name = "gemini-1.5 flash"

    def research_theme(self, prompt: str, theme) -> str:
        # Placeholder for actual API call to Gemini model
        return f"Generated text for prompt: {prompt}"
