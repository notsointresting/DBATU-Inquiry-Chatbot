# Importing libs and modules
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains.question_answering import load_qa_chain
from fastapi import FastAPI
from pydantic import BaseModel
import os
import time
from dotenv import load_dotenv

# Setting Google API Key
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Path of vectore database
DB_FAISS_PATH = 'vectorstore/db_faiss'




# Prompt template
custom_prompt_template = """
    Act as chatbot provided by Dr. Babasaheb Ambedkar Technological University, Lonere.
      Whenever user says Hi, You should respond with Greeting and welcome user to university's chatbot. 
      Answers of queires asked by user should from given documents only. Try to give the best and correct answer only.    
    Also try to add some your own wordings the describe the answer.Don't greet.

    Use the following pieces of information to answer the user's question.\n
    Context: {context}
    Question: {question}
     
    Try to give the best and correct answer only.
    Also try to add some your own wordings the describe the answer.
    if website link is available in given context then only, try to provide website links from given context only. else don't provide any website link.
    Helpful Answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt



#Loading the model
def load_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.6)
    return llm


# Setting QA chain
def get_conversational_chain():

    prompt = set_custom_prompt()
    
    llm = load_llm()
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    return chain

# User input function
def user_input(user_question):
    
    # Set google embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    # Loading saved vectors from local path
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    docs = db.similarity_search(user_question)
    
    chain = get_conversational_chain()
    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    return response


'''lst_questions = [
    "Where is the university located?",
    "What courses does the university offer?",
    "How can I apply for admission?",
    "What is the fee for the courses?",
    "Does university offers hostels?",
    "Who is the head of the university?",
    "Does the university have a library, is there any digital library?",
    "What sports does the university offer?",
    "Does the university have a canteen?",
    "What is the university's contact number?",
    "Does the university have a website?",
    "What is the university's email address?",
    "Does the university offer scholarships?",
    "What is the university's ranking?",
    "Does the university have a placement cell?",
    "What is the university's history?",
    "Does the university have a research center?",
    "What is the university's mission?",
    "Does the university have a student council?",
    "What is the university's attendance policy?",
    "Does the university have a medical center?",
    "What is the university's exam schedule?",
    "Does the university have a computer lab?",
    "What is the university's grading system?",
    "Does the university have an alumni association?",
    "What is the university's dress code?",
    "Does the university have a music club?",
    "What is the university's academic calendar?",
    "Does the university have a science lab?",
    "Does the university have a cultural fest?",
    "Who is Pramod?"
]'''

start = time.time()
while True:
    question = input("Enter your question: ")
    with open('FAQ-1.txt', 'a') as f:
        f.write('Q.' + question + "\n")
        f.write('Answer:  ' + user_input(question)['output_text'] )
        f.write('\n')
        f.write("\n")
        time.sleep(5)
end = time.time()

print("Time taken to answer all the questions: ", end-start)
