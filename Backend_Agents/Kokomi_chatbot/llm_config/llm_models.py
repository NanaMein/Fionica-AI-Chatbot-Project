import os
from langchain_groq import ChatGroq
from llama_index.llms.groq import Groq
from dotenv import load_dotenv

load_dotenv()

def manager_agent_llm() -> ChatGroq:
    return ChatGroq(
        model=os.getenv(''), api_key=os.getenv(''), temperature=.5
    )

def worker_agent_llm() -> ChatGroq:
    return ChatGroq(
        model=os.getenv(''), api_key=os.getenv(''), temperature=.5, max_tokens=1000
    )

def rag_llm() -> Groq:
    return Groq(api_key=os.getenv(''), model=os.getenv('')
    )