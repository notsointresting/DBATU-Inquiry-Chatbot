import os
from dotenv import load_dotenv
import openai
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")
OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_ADA_EMBEDDING_MODEL_NAME = os.getenv("OPENAI_ADA_EMBEDDING_MODEL_NAME")

# Ensure all necessary environment variables are set
if not all([OPENAI_API_KEY, OPENAI_DEPLOYMENT_ENDPOINT, OPENAI_DEPLOYMENT_VERSION, OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME, OPENAI_ADA_EMBEDDING_MODEL_NAME]):
    raise EnvironmentError("One or more environment variables are missing. Please check your .env file.")

# Initialize OpenAI API settings for Azure
openai.api_type = "azure"
openai.api_version = OPENAI_DEPLOYMENT_VERSION
openai.api_key = OPENAI_API_KEY

def generate_embeddings():
    try:
        # Initialize OpenAI embeddings with Azure settings
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME,
            azure_endpoint=OPENAI_DEPLOYMENT_ENDPOINT,
            model=OPENAI_ADA_EMBEDDING_MODEL_NAME,
            chunk_size=1
        )

        # Define the path to the PDF file
        file_path = os.path.join(os.getcwd(), "data", "List_Q&A_Part_2.pdf")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Load and split the PDF document using Langchain's PDF loader
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()

        # Create embeddings for the document pages using text-embedding-ada-002
        db = FAISS.from_documents(documents=pages, embedding=embeddings)

        # Save the embeddings into a local FAISS vector store
        db.save_local("./dbs/documentation/faiss_index")

        print("Embeddings generated and saved successfully.")

    except openai.error.OpenAIError as e:
        print(f"OpenAI error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    generate_embeddings()
