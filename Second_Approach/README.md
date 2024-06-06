# Building a University Chatbot with Azure OpenAI Service and Langchain
---

## Introduction
The chatbot will be able to answer questions related to universities, admission, and fees. We will leverage the LangChain library, which incorporates services like OpenAI and Azure to provide intelligent responses.

## Key Concepts
Before we dive into the code, let's understand some key concepts:
- LangChain: LangChain is a Python library that allows us to build conversational AI models using various language models and vector stores.

- OpenAI: OpenAI is an artificial intelligence research laboratory that provides powerful language models for natural language processing tasks.

- Azure: Azure is a cloud computing service provided by Microsoft. We will use Azure to deploy our chatbot and utilize its AI capabilities.

- FAISS: FAISS is a library for efficient similarity search and clustering of dense vectors. We will use FAISS to store and search for similar documents.

- OpenAI API: The OpenAI API provides access to powerful language models that can generate human-like responses to user queries.

- Conversational Retrieval Chain: A conversational retrieval chain is a model that retrieves relevant responses from a knowledge base based on the user's input.

- Embeddings Model: An embeddings model converts text into numerical representations called embeddings, which capture the semantic meaning of the text. These embeddings can be used for various natural language processing tasks, such as similarity searches.

- Question Identification: The chatbot system includes functions for identifying different question types, such as those related to identity, university, or fees. These functions check if the user's input contains specific keywords related to each question type.
---

## Code Structure

- Import Statements: The script imports necessary modules and classes from various libraries, including OpenAI, langchain, and the identify_filter file.

- Environment Variable Configuration: The script loads environment variables required for the OpenAI API and other configurations.

- Question Identification Functions: The identify_filter file contains functions for identifying different question types. These functions check if the user's input contains specific keywords related to each question type.

- Main Execution Code: The main execution code initializes the OpenAI API, sets up the conversational retrieval chain, and creates an embeddings model. It also loads a FAISS vector store and configures a prompt template for generating standalone questions. The code then enters a continuous interaction loop, where it prompts the user for input, identifies the question type, and provides appropriate responses based on the question type.
---

## Code Example

### Configuration Variables
```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
# ... (other configuration variables)
```
This section retrieves configuration variables, such as the OpenAI API key, deployment endpoint, and other settings, from environment variables.
---

### Question Identification Functions:
```python
def is_question_about_identity(user_input):
    identity_keywords = ["who made this", "creator", "owner", "origin", "made by", "developer", "author"]
    return any(keyword in user_input.lower() for keyword in identity_keywords)

def is_question_related_to_university(user_input):
    university_keywords = ["university", "admission", "college", "degree", "education", "campus", "major", "courses", "enrollment", "academic"]
    return any(keyword in user_input.lower() for keyword in university_keywords)

def is_question_about_fees(user_input):
    fees_keywords = ["fees", "fee structure", "tuition", "cost"]
    return any(keyword in user_input.lower() for keyword in fees_keywords)
```
Here, functions are defined to check if a given user input corresponds to specific question types, including identity-related questions, university-related questions, and questions about fees.
---
### Vector Store Initialization
```python
vectorStore = FAISS.load_local("./dbs/documentation/faiss_index", embeddings)
retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})
```

The script initializes a FAISS vector store from a local file and sets up a retriever for similarity searches.
---
### Main Loop for Chatbot Interaction:
```python
while True:
    query = input('you: ')
    if query == 'q':
        break
    # ... (code for identity, university, and fees-related checks)
    chat_history = ask_question_with_context(qa, query, chat_history)
    print()
```

The script enters a continuous loop where the chatbot interacts with the user. It reads user input, checks for special commands like 'q' to quit, performs checks for different question types, and generates responses using the conversational retrieval chain.
---

## Code Explaination

#### Let's go through the code step by step:

- We import the necessary libraries and modules, including the LangChain library and the identify_filter module, which contains functions to filter specific question categories.

- We load the environment variables using the load_dotenv() function. This allows us to securely store sensitive information like API keys.

- We configure the OpenAI API for Azure by setting the necessary variables.

- We initialize the AzureChatOpenAI and OpenAIEmbeddings models using the provided deployment names, model names, API endpoints, and API keys.

- We load the FAISS vector store that we previously saved into memory. This vector store is used for similarity-based searches.

- We set up the retriever using the FAISS vector store. This allows us to search for similar documents based on user queries.

- We define a prompt template for rephrasing questions. This template is used to convert follow-up questions into standalone questions.

- We create a conversational retrieval chain using the AzureChatOpenAI model, the retriever, and the prompt template. This chain is responsible for generating responses based on user queries.

- We enter a loop for user interaction. Inside the loop, we take user input and check for specific question categories using the identify_filter module.

- If the question is about the identity of the chatbot, we respond accordingly.

- If the question is not related to universities or admission, we inform the user that the question is not relevant.

- If the question is about fees, we provide a link to the fees structure of the university.

- For university-related questions, we use the `ask_question_with_context()` function to generate a response based on the user query and the chat history.

- Finally, we print the response and continue the loop for further user interaction.


