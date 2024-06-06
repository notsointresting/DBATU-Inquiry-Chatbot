from dotenv import load_dotenv
import os
import openai
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

from identify_filter import is_question_about_identity, is_question_related_to_university

#load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_DEPLOYMENT_NAME")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_DEPLOYMENT_VERSION = os.getenv("OPENAI_DEPLOYMENT_VERSION")
OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME = os.getenv("OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME")
OPENAI_ADA_EMBEDDING_MODEL_NAME = os.getenv("OPENAI_ADA_EMBEDDING_MODEL_NAME")

openai_model = AzureChatOpenAI(
    deployment_name=OPENAI_DEPLOYMENT_NAME,
    model_name=OPENAI_MODEL_NAME,
    openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT,
    openai_api_version=OPENAI_DEPLOYMENT_VERSION,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type="azure"
)

def ask_question_with_context(qa, openai_model, question, chat_history):
    query = question

    # Use the QA model to get an answer
    result = qa({"question": question, "chat_history": chat_history})
    answer = result["answer"]

    # Append the question and answer from the QA model to the chat history
    chat_history.append((query, answer))

    # Check if the question is present in your dataset
    for history, _ in chat_history:
        if query.lower() in history.lower():
            return chat_history  # If found, return the existing answer

    # If not present, use OpenAI's model to generate a response
    response = openai_model([{"prompt": query, "chat_history": chat_history}])

    # Extract the generated response from the model output
    generated_response = response[0]["choices"][0]["text"]

    # Append the new question and generated answer to the chat history
    chat_history.append((query, generated_response))

    return chat_history






if __name__ == "__main__":
    # Configure OpenAI API
    openai.api_type = "azure"
    openai.api_base = os.getenv('OPENAI_API_BASE')
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_version = os.getenv('OPENAI_API_VERSION')

    llm = AzureChatOpenAI(deployment_name=OPENAI_DEPLOYMENT_NAME,
                      model_name=OPENAI_MODEL_NAME,
                      openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT,
                      openai_api_version=OPENAI_DEPLOYMENT_VERSION,
                      openai_api_key=OPENAI_API_KEY,
                      openai_api_type="azure")
    
    embeddings=OpenAIEmbeddings(deployment=OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME,
                                model=OPENAI_ADA_EMBEDDING_MODEL_NAME,
                                openai_api_base=OPENAI_DEPLOYMENT_ENDPOINT,
                                openai_api_type="azure",
                                chunk_size=1)

    # Initialize gpt-35-turbo and our embedding model
    #load the faiss vector store we saved into memory
    vectorStore = FAISS.load_local("./dbs/documentation/faiss_index", embeddings,allow_dangerous_deserialization=True)

    #use the faiss vector store we saved to search the local document
    retriever = vectorStore.as_retriever(search_type="similarity", search_kwargs={"k":2})

    QUESTION_PROMPT = PromptTemplate.from_template("""
    Given the context provided in the conversation, your task is to generate a relevant and informative response to the user's query about DBATU (Dr. Babasaheb Ambedkar Technological University). Your response should address the specific question asked while providing accurate and up-to-date information about the university. If there are relevant links or resources available, please include them in your response. If the answer is not available in the current dataset, you may use OpenAI's dataset to provide additional context or information.
    Context:
    {chat_history}

    User Query: {question}

    Response:

""")
    
   

    qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                            retriever=retriever,
                                            condense_question_prompt=QUESTION_PROMPT,
                                            return_source_documents=True,
                                            verbose=False)


    chat_history = []

    


    
    

    while True:
        query = input("User: ")
        # Rest of your code (process university-related questions)
        chat_history = ask_question_with_context(qa,openai_model, query, chat_history)
        with open("chat_history_3.txt", "a") as f:
            f.write("User: "+query + "\n")
            f.write("-> "+chat_history[-1][1] + "\n")
            f.write('\n')
        print()
        
