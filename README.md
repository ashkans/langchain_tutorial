# LangChain Tutorial Repository

Welcome to the **LangChain Tutorial Repository**! This project is dedicated to walking through the LangChain tutorial series, providing hands-on experience with Language Model (LLM) applications and LangChain’s powerful abstractions.

## Repository Structure

- **`nbs/`**: Contains subdirectories for each tutorial, complete with corresponding code and resources.
- **`langchain_tutorial/`**: Contains shared code and utilities used across multiple tutorials.

## Tutorials

### 1. Basics

These foundational tutorials will introduce you to the core concepts and capabilities of LangChain, including building basic LLM applications, chatbots, and exploring how LangChain enhances LLM workflows with vector stores and agents.

1.1. [x] [**Build a Simple LLM Application with LCEL**](https://python.langchain.com/docs/tutorials/llm_chain/)

- In this tutorial, you'll learn how to create a basic Language Model application using **LangChain Expression Language (LCEL)**, a powerful framework for chaining language models together. This is ideal for anyone just getting started with LangChain, covering the essentials of model chaining and task automation.

  1.2. [x] [**Build a Chatbot**](https://python.langchain.com/docs/tutorials/chatbot/)

- Go a step further by building a chatbot that can remember the conversation history and provide personalized responses. This tutorial also dives into techniques for managing large conversation histories, maintaining context, and using streaming to deliver real-time user interaction — a must for those interested in conversational AI.

  1.3. [x] [**Vector Store and Retrieval**](https://python.langchain.com/docs/tutorials/retrievers/)

- Learn how to efficiently retrieve relevant data for your LLM workflows using LangChain's **vector store** and **retriever** abstractions. This tutorial is perfect for those looking to improve LLM responses by providing the model with external knowledge or relevant context through **Retrieval-Augmented Generation (RAG)** techniques.

  1.4. [x] [**Build an Agent**](https://python.langchain.com/docs/tutorials/agents/)

- Agents are autonomous systems that can make decisions, retrieve information, and take actions. This tutorial will guide you through creating an agent that can interact with various environments or APIs, allowing for dynamic decision-making and task completion. Ideal for building more interactive and complex LLM applications.

### 2. LangGraph (Agents)

This section will focus on building and deploying LangChain agents using **LangGraph**, a toolset for orchestrating agents in a structured and modular way. These tutorials will teach you how to manage multi-step workflows, and handle decision-making chains in complex systems.

2.1 [ ] Tutorial in progress.

### 3. Working with External Knowledge

These tutorials explore how to extend your LLM's capabilities by connecting it with external data sources, making your applications more intelligent and context-aware.

3.1 [ ] [**Build a Retrieval-Augmented Generation (RAG) Application**](<https://python.langchain.com/docs/tutorials/#:~:text=Build%20a%20Retrieval%20Augmented%20Generation%20(RAG)%20Application>)

- In this tutorial, you'll learn how to build a **Retrieval-Augmented Generation (RAG)** application that integrates external data (e.g., databases, documents, APIs) into your LLM's responses. This approach significantly improves the relevance and accuracy of generated content, making it ideal for real-world applications like Q&A systems, document retrieval, and personalized assistants.

More tutorials will be added as the series progresses, covering advanced topics like real-time data integration, custom agent designs, and more.

## Getting Started

1. **Clone** this repository:
   ```bash
   git clone <repo_url>
   ```
