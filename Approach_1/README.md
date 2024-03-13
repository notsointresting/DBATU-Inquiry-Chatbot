# Table of Contents

1. [Introduction](#introduction)
2. [Key Concept](#key-concepts)
3. [Code Structure](#code-structure)
4. [Code Examples](#code-examples)
5. [Conclusion](#conclusion)
6. [Steps To Run Code](#steps-to-run-code)
  



# Introduction

This code allows users to chat with multiple PDF files. It utilizes the Palm and Langchain libraries for natural language processing and conversational retrieval. Users can upload PDF files, ask questions, and receive responses from a chatbot.

## Key Concepts

- **Palm:** The Palm library is used for generating embeddings of text. It provides a way to represent text as numerical vectors, which can be used for various NLP tasks.

- **Langchain:** Langchain is a library that combines different components for conversational retrieval. It includes a language model, memory, and vector store to enable chatbot-like interactions.

- **Streamlit:** Streamlit is a Python library used for building interactive web applications. It provides an easy-to-use interface for creating UI elements and handling user input.

## Code Structure

The code is structured into several functions and a main function. Here's an overview of the main functions:

- `get_conversational_chain(vector_store)`: Creates a conversational retrieval chain using the Langchain library. It takes a vector store as input and returns a conversation chain object.

- `get_pdf_text(pdf_docs)`: Extracts the text from the uploaded PDF files using the PyPDF2 library to read the PDFs and extract the text from each page.

- `get_text_chunks(text)`: Splits the extracted text into smaller chunks using a recursive character-based text splitter to divide the text into chunks of a specified size.

- `get_vector_store(text_chunks)`: Generates embeddings for the text chunks using the Palm library. It creates a vector store using the FAISS library, which allows for efficient similarity search.

- `Processing_data(pdf_docs)`: Processes the uploaded PDF files by extracting text, splitting it into chunks, and generating embeddings. It also initializes the conversation chain.

- `user_input(user_question)`: Handles user input and generates responses from the chatbot. It takes a user question as input and uses the conversation chain to generate a response.

- `main()`: The main function that sets up the Streamlit application. It configures the page title, creates the UI elements, and handles user interactions.

## Code Examples

Here are a few code examples to illustrate how the functions are used:

1. Creating a conversation chain:

    ```python
    vector_store = get_vector_store(text_chunks)
    conversation_chain = get_conversational_chain(vector_store)
    ```

2. Processing PDF files:

    ```python
    def Processing_data(pdf_docs):
    with st.spinner("Processing"):
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        vector_store = get_vector_store(text_chunks)
        st.session_state.conversation = get_conversational_chain(vector_store)
    ```

3. Handling user input and generating responses:

    ```python
    def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        key = f"chat_widget_{i}"  # Generate a unique key for each chat widget
        if i % 2 == 0:
            cht.message(f"Human: {message.content}", is_user=True, key=key)
        else:
            cht.message(f"Bot: {message.content}", key=key)  
    ```

# Conclusion

This code provides a simple way to chat with multiple PDF files. It uses the Palm and Langchain libraries for natural language processing and conversational retrieval. By uploading PDF files and asking questions, users can interact with a chatbot-like system and receive responses based on the content of the PDFs.

# Steps To Run Code!

## STEP 01:
CREATE CODESPACE, MAIN BRANCH

## STEP 02:
Install all libraries, for that use below command in terminal.

```bash
cd Approach_1
pip install -r requirement.txt
```

## STEP 03:
Go to this [Site](https://makersuite.google.com/app/apikey), and select **CREATE API KEY IN NEW PROJECT**, and copy the API Key

## STEP 04:
In Terminal
```bash
code P*
```

In Code, Go to Line No. 13,
Replace the line with API key generated.

```python
os.environ['GOOGLE_API_KEY'] = "GOOGLE_API_KEY"
```

## STEP 05:
Ready to run, 
To Run code use below command!

```bash
streamlit run P*
```
