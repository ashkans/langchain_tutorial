from langchain_core.prompts import ChatPromptTemplate

message = """
Answer this question using the provided context only. If there is not enough information say I dont know, but in a more polite way.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message)])
