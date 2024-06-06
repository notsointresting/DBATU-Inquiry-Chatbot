# Explaination of Codes as Followed
---

## Table of Contents

1. [news_scrapper.py](#news_scrapperpy)
2. [app_embeddings.py](#app_embeddingspy)
3. [main.py](#mainpy)
4. [app.py](#apppy)




### news_scrapper.py
The Code is responsible for gathering latest up to date information from the university's website.

## Key Concepts
To understand the code, let's go over some key concepts:

- **Web Scraping**: The process of extracting data from websites. In this code, we use the requests library to send HTTP requests to the specified URLs and retrieve the HTML content of the web pages. We then use the BeautifulSoup library to parse the HTML and extract the desired information.

- **PDF Generation**: The process of creating a PDF file programmatically. In this code, we use the FPDF library, which provides a simple interface for creating PDF documents. We can add text, images, and other elements to the PDF using the library's methods.

- **File Handling**: The process of manipulating files on the computer. In this code, we use the os module to check if a PDF file with the specified name already exists and remove it if necessary. We also use the os.path module to construct the file path for the PDF.

## Code Structure
The code is structured into three main parts:

1. The `get_latest_news` function fetches the latest news articles from a given URL. It uses the requests library to send an HTTP GET request to the URL and retrieve the HTML content of the web page. It then uses the **BeautifulSoup** library to parse the HTML and extract the news title, link, and date for each article. The function returns a list of dictionaries, where each dictionary represents a news article and contains the title, link, and date.

2. The `create_pdf` function generates a PDF file containing the latest news from both URLs. It uses the **FPDF** library to create a new PDF document and adds the news details **(title, link, date)** to the PDF, organized by source. The function takes two lists of news articles (one for each URL) and a filename as input.

3. The main function orchestrates the process. It first removes any existing PDF file with the specified name to avoid duplicates. It then fetches the latest news from both URLs using the `get_latest_news` function. Finally, it calls the `create_pdf` function to create a new PDF file named **'latest_news.pdf'** with the compiled news information.

You Can check the format of feteched news by going into [this.](data/latest_news.pdf)


### app_embeddings.py

This code performs the task of creating vector embeddings for text content in PDF documents. Vector embeddings are numerical representations of text that capture its semantic meaning. These embeddings enable efficient similarity searches and other natural language processing (NLP) tasks.

## Key Concepts
Before diving into the code, let's understand some key concepts:

- **Vector Embeddings**: Vector embeddings are numerical representations of text that capture its semantic meaning. These embeddings are generated using machine learning models trained on large amounts of text data.

- **PDF Documents**: PDF (Portable Document Format) is a file format used for representing documents in a manner independent of the software, hardware, and operating system. PDF documents can contain text, images, and other elements.

- **FAISS**: FAISS (Facebook AI Similarity Search) is a library for efficient similarity search and clustering of dense vectors. It provides a fast and memory-efficient solution for indexing and searching vector embeddings.

- **Google Generative AI**: Google Generative AI is a suite of machine learning models developed by Google. These models can be used for various NLP tasks, including text embedding generation.

## Code Structure
The code is structured as follows:

1. Fetch Latest News: The code calls the main() function from the `news_scrapper` module to fetch the latest news and generate a PDF file.

2. Load Environment Variables: The code uses the dotenv library to load the **Google API** key from the environment variables.

3. Load PDF Documents: The code reads all PDF documents from the specified directory (data/) using the **DirectoryLoader** and **PyPDFLoader** classes.

4. Split Text into Chunks: The code uses the **RecursiveCharacterTextSplitter** class to split the text content of the PDF documents into smaller chunks. This is done to process the text in batches and avoid memory limitations.

5. Generate Text Embeddings: The code uses Google's Generative AI to generate vector embeddings for the text chunks. The **GoogleGenerativeAIEmbeddings** class is used for this purpose.

6. Batch Processing: The code processes the text chunks in batches. It embeds the text chunks using the Google Generative AI model and adds them incrementally to a **FAISS vector store**. A delay of 1 minute is added after processing each batch to avoid rate limits.

7. Save Vector Store: The code saves the FAISS vector store containing the text embeddings locally.

Here are some code examples to illustrate the functionality of the code:

- Fetch Latest News:
```python
from news_scrapper import main

main()
```

- Load PDF Documents:
```python
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

DATA_PATH = 'data/'

loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
documents = loader.load()
```

- Split Text into Chunks:
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
texts = text_splitter.split_documents(documents)
```

- Generate Text Embeddings:
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
batch_embeddings = embeddings.embed_documents(batch_content)
```

- Batch Processing:
```python
batch_size = 50
total_texts = len(texts)

for i in range(0, total_texts, batch_size):
    batch = texts[i:i + batch_size]
    batch_content = [doc.page_content for doc in batch]
    # Process the batch and add embeddings to the vector store
```

- Save Vector Store:
```python
from langchain_community.vectorstores import FAISS

DB_FAISS_PATH = 'vectorstore/db_faiss'

db.save_local(DB_FAISS_PATH)
```

## main.py

This code defines a chatbot system that answers user queries about Dr. Babasaheb Ambedkar Technological University using Google's Generative AI and a vector database for question answering. The chatbot is designed to provide accurate and context-aware responses to queries related to the university.

### Key Concepts

- Google's Generative AI: The chatbot system utilizes Google's Generative AI model, specifically the **"gemini-1.5-flash-latest"** model, to generate responses to user queries. This model is trained on a large corpus of text data and is capable of generating human-like responses.

- Vector Database: The chatbot system uses a vector database, implemented using the FAISS library, to store pre-computed document embeddings. These embeddings are used to retrieve relevant documents based on user queries, enabling the chatbot to provide accurate responses.

- Question Answering Chain: The chatbot system sets up a question-answering chain that combines the Generative AI model and the vector database. This chain takes user queries as input, retrieves relevant documents from the vector database, and generates responses using the Generative AI model.

## Code Structure
The code is structured into several sections:

1. **Imports and Initial Setup**: This section imports the necessary libraries and modules for AI, vector store, and environment management. It also loads the Google API key from environment variables.

2. **Path and Prompt Template**: This section defines the path to the **FAISS vector database** and creates a custom prompt template that guides the AI on how to respond to questions about the university.

3. **Functions**: This section defines several functions used in the chatbot system, including functions for setting the custom prompt, loading the language model, setting up the question-answering chain, and processing user input.

4. **Usage Flow**: This section outlines the flow of the chatbot system, including loading environment variables, defining paths and prompts, loading and setting up models, and processing user input.

Here are some code examples to illustrate the usage of the chatbot system:

- Setting up the custom prompt template:

```python
custom_prompt_template = """
    You are an intelligent assistant helping the users with their questions about admission information, information related to university, exam queries, 
    at Dr. Babasaheb Ambedkar Technological University and
    you also know multiple human language spoken in India, so you are basically multilingual and you know marathi language also.
    Formatting
    You can send formatted text messages to Capacities, using the following syntax:
    - for bullets
    **text** for bold text

    Rules:
    Strictly use ONLY the following pieces of context to answer the question.
    If you have external knowledge about the question, provide a answer. 
    If users greets you, you should also greet them back and you are chatbot provided by Dr. Babasaheb Ambedkar Technological University.
    If any website link is provided along the context provide it also but if not then don't provide any website.
    If the question is not related to university, you should say "Please ask question related to university".
    Maintain the chat history and context of the conversation. 
    


Do not try to make up an answer:
    If the context is empty, just say "not enough information provided, but here is link to the official website: https://dbatu.ac.in/"

CONTEXT:
{context}

QUESTION:
{question}

Helpful Answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt
```

- Loading the language model:

```python
def load_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.6)
    return llm

```
- Setting up the question-answering chain:


```python
def get_conversational_chain():
    prompt = set_custom_prompt()
    llm = load_llm()
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    return chain
```
- Processing user input and generating a response:

```python
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    return response
```

### app.py
It set up a Flask web application that integrates with a Telegram bot. The bot will use Google's Generative AI to provide intelligent responses to user queries. 

## Key Concepts


- **Flask**: Flask is a micro web framework written in Python. It allows us to build web applications easily and quickly.

- **Telegram Bot API**: Telegram provides a Bot API that allows developers to interact with Telegram bots. We will use this API to send and receive messages from our bot.

- **Google Generative AI**: Google's Generative AI is a powerful language model that can generate human-like text based on given prompts. We will leverage this AI model to generate intelligent responses to user queries.



## Code Structure
The code provided consists of several sections, each serving a specific purpose. Let's go through each section and understand its functionality:

1. **Imports and Initial Setup**: This section imports the necessary libraries and modules for Flask, Google Generative AI, environment variable management, and the `user_input` function from `main.py`. It also loads the environment variables using dotenv.

2. **Google Generative AI Configuration**: Here, we configure the Google Generative AI with the API key obtained from the environment variables.

3. **Flask App and Telegram Bot Setup**: This section initializes a Flask app and retrieves the Telegram Bot Token from the environment variables.

4. **Helper Functions**: This section contains three helper functions:

    - **generate_answer(question)**: This function uses the `user_input` function to generate an answer to the user's question by calling the language model and retrieving the output text.

    - **message_parser(message)**: This function parses incoming messages from Telegram to extract the chat ID and message content. It handles both text and voice messages and returns the chat ID, message content, and message type.

    - **send_message_telegram(chat_id, text)**: This function sends a text message to the specified chat ID on Telegram using the Telegram Bot API.

5. **Flask Routes**: This section defines the routes for the Flask app:

    - index(): This route handles both GET and POST requests. For POST requests, it parses the incoming message JSON, extracts the chat ID and content using the `message_parser` function, generates an appropriate response based on the message type, and sends the generated response back to the user on Telegram. For GET requests, it returns a simple HTML message indicating an error.

6. **Main Application Entry Point**: This section runs the Flask app on 0.0.0.0 at port 5000 with debug mode disabled.


Let's take a look at some code examples to better understand how the different components work together:

1. Example of generating an answer using the `generate_answer` function:
```python
def generate_answer(question):
    answer = user_input(question)['output_text']
    return answer
```
2. Example of parsing incoming messages using the `message_parser` function:

```python
def message_parser(message):
    try:
        chat_id = message['message']['chat']['id']
        if 'text' in message['message']:
            text = message['message']['text']
            return chat_id, text, 'text'
        elif 'voice' in message['message']:
            file_id = message['message']['voice']['file_id']
            return chat_id, file_id, 'voice'
        else:
            return chat_id, None, None
    except KeyError as e:
        return None, None, None
```
3. Example of sending a message to Telegram using the `send_message_telegram` function:

```python
def message_parser(message):
    try:
        chat_id = message['message']['chat']['id']
        if 'text' in message['message']:
            text = message['message']['text']
            return chat_id, text, 'text'
        elif 'voice' in message['message']:
            file_id = message['message']['voice']['file_id']
            return chat_id, file_id, 'voice'
        else:
            return chat_id, None, None
    except KeyError as e:
        return None, None, None
```