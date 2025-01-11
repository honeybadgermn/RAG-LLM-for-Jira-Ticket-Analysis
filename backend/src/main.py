import os
import requests
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from src.rag_retriever import RAGRetriever

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "ollama")
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")

retriever = RAGRetriever()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/query")
def query_rag(user_query: str = Body(..., embed=True)):
    docs = retriever.get_relevant_docs(user_query)

    context = "\n\n".join(docs)
    
    print("[DEBUG] Context for LLM prompt:\n", context)

    prompt = f"""
    Below is a list of tickets. Each chunk shows "Issue key", "Status", "TADS Affected System(s)", and "Summary".

    Please answer the user’s question using only these ticket lines. If you need to count them, list them first, then give the total. If any info is missing, say "I don’t know."

    Ticket Lines:
    {context}

    Question: {user_query}
    Answer:
    """

    url = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"
    payload = {
        "prompt": prompt,
        "model": "llama2",
        "stream": False
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        llm_answer = response.json().get("response", "")
    else:
        llm_answer = f"Error calling Ollama: {response.text}"

    return {"answer": llm_answer}
