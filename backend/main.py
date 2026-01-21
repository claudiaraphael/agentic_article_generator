import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


def get_llm(provider="gemini"):
    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-1.5-flash-latest",
            google_api_key=os.getenv("GEMINI_API_KEY")
        )
    else:
        # Using a free Hugging Face model (Mistral) via API
        return HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.2",
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
        )


def generate_linkedin_article(topic, provider="gemini"):
    llm = get_llm(provider)

    template = """
    You are a professional LinkedIn Content Creator.
    Write a high-quality, SEO-optimized article about: {topic}
    
    Structure:
    - Catchy Hook
    - 3 Main Points
    - Conclusion with a Call to Action
    - 5 relevant hashtags
    """

    prompt = PromptTemplate.from_template(template)

    # This is a simple LangChain Chain (LCEL)
    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"topic": topic})



# aqui eu baixo a llm, baixo o tokenizador, faço o fine tuning e salvo o modelo ajustado
# e testo o modelo ajustado
if __name__ == "__main__":
    topic = "The Future of AI in Healthcare"
    article = generate_linkedin_article(topic, provider="gemini")
    print(article)