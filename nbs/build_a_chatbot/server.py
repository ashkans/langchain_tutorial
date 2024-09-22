#!/usr/bin/env python
from fastapi import FastAPI
from langserve import add_routes
import dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

dotenv.load_dotenv()
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. Answer all questions to the best of your ability in {language}.",
    ),
    MessagesPlaceholder(variable_name="history"),
    (
        "human",
        "{human_input}",
    ),
])

chain = prompt | ChatOpenAI()


class InputChat(BaseModel):
    """Input for the chat endpoint."""

    # The field extra defines a chat widget.
    # As of 2024-02-05, this chat widget is not fully supported.
    # It's included in documentation to show how it should be specified, but
    # will not work until the widget is fully supported for history persistence
    # on the backend.
    human_input: str = Field(
        ...,
        description="The human input to the chat system.",
        extra={"widget": {
            "type": "chat",
            "input": "message"
        }},
    )

    language: str = Field(
        ...,
        description="Language to response",
        extra={"widget": {
            "type": "chat",
            "input": "language"
        }},
    )


chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="human_input",
    history_messages_key="history").with_types(input_type=InputChat)

add_routes(
    app,
    chain_with_history,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
