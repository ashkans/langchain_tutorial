#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langserve import add_routes
from prompt import prompt
from vectore_store import retriever

# 1. Create prompt template

# 2. Create model
model = ChatOpenAI()

rag_chain = {
    "context": retriever,
    "question": RunnablePassthrough()
} | prompt | model

# 4. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route
add_routes(
    app,
    rag_chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
