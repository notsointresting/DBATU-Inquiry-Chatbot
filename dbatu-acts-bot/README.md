# Chatbot for Answering User Queries using PDF Data

## Introduction
In this article, we will discuss how to create a chatbot that can answer user queries using PDF data. The chatbot utilizes the Gemini-Pro model by Google and the Langchain library. The code provided includes the embedding code and the main code for the chatbot.

## Key Concepts
Before diving into the code, let's understand some key concepts:

- **Langchain**: Langchain is a library that provides various functionalities for natural language processing tasks, such as text splitting, document loading, and vector stores.

- **Google Generative AI**: Google Generative AI is a powerful AI model developed by Google that can generate human-like responses to user queries.

- **FAISS**: FAISS is a library for efficient similarity search and clustering of dense vectors. It is used to store and retrieve text embeddings.

- **PDF Loader**: The PDF loader is a module in Langchain that allows loading PDF documents for further processing.

## Code Structure
The provided code is divided into two sections: the embedding code and the main code.

### `Embedding code`
The embedding code is responsible for converting the text data from PDF documents into vector embeddings. Here's a breakdown of the code:

1. Importing the required modules and libraries.
2. Setting the path for input data files and the vector store.
3. Configuring the Google Gemini API key.
4. Defining a function to create the vector database.
5. Loading the PDF documents using the PDF loader.
6. Splitting the text into chunks.
7. Using the Google Generative AI embeddings to convert the text chunks into vector embeddings.
8. Saving the embeddings in the vector store.

### Main Code
The main code is responsible for creating the chatbot and answering user queries. Here's a breakdown of the code:

- **Importing Libraries**: The script imports necessary libraries and modules, including Langchain for natural language processing, Google Generative AI for generating responses, and FAISS for similarity search and clustering of dense vectors.

- **Setting Up API Key and Paths**: It sets up the Google API key and the path for the vector database.

- **Prompt Template**: It defines a custom prompt template for the question-answering process.

- **Loading the Model**: It loads the Gemini-Pro model from Google Generative AI.

- **Setting Up the Conversational Chain**: It sets up the conversational chain for question-answering using the loaded model and the custom prompt template.

- **User Input Function**: It defines a function to handle user input. This function loads the saved vectors from the local path, performs a similarity search on the user's question, gets the conversational chain, and returns the chatbot's response.

- **Question List**: It defines a list of questions to ask the chatbot.

- **Writing Answers to File**: It iterates over the list of questions, and for each question, it writes the question and the chatbot's response to a file named 'FAQ-5.txt'.

- **Time Calculation**: It calculates the time taken to answer all the questions and prints it out.


## Code Examples
Here are some code examples to illustrate the usage of the provided code:

- Creating the vector database:
```python
create_vector_db()
```


Answering a list of questions and writing the answers to a file:
```python
lst_questions = [
    "Where is the university located?",
    "What courses does the university offer?",
    "How can I apply for admission?",
    ...
]

for question in lst_questions:
    with open('FAQ-5.txt', 'a') as f:
        f.write('Q.' + question + "\n")
        f.write('Answer:  ' + user_input(question)['output_text'])
        f.write('\n')
        f.write("\n")
```

## Installation and Running the Code

Follow these steps to install the necessary libraries and run the Python code:

1. **Clone the Repository**: First, clone the repository to your local machine using Git.

```bash
git clone <repository-url>
```

2. **Navigate to the Directory**: Navigate to the directory containing the Python script and the requirements.txt file.

```bash
cd <directory-name>
```

3. **Create a Virtual Environment**: It's a good practice to create a virtual environment before installing the libraries. You can do this using the venv module in Python.

```bash
python3 -m venv env
```

4. **Activate the Virtual Environment**: Activate the virtual environment. The command to do this varies based on your operating system.

- On Windows:

```bash
.\env\Scripts\activate
```

- On Unix or MacOS:

```bash
source env/bin/activate
```

5. **Install the Libraries**: Install the necessary libraries using pip. The libraries are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

6. Run **the Python Script**: Finally, you can run the Python script.

```bash
python <script-name>.py
```

