# Importing libs and modules
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import os
from dotenv import load_dotenv


# Setting Google API Key
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('API_KEY')
genai.configure(api_key=os.getenv("API_KEY"))



# Path of vectore database
DB_FAISS_PATH = 'vectorstore/db_faiss'


# Prompt template
custom_prompt_template = """
    You are an intelligent assistant helping the users with their questions about there CGPA, Student will give there unique PRN
    Your job is to give them there CGPA and if user ask by name to get cgpa or sgpa.
    you also know multiple human language spoken in India, so you are basically multilingual and you know marathi language also.


    Rules:
    Strictly use ONLY the following pieces of context to answer the question.
    If users greets you, you should also greet them back and you are chatbot provided by Dr. Babasaheb Ambedkar Technological University.
    If any website link is provided along the context provide it also but if not then don't provide any website.
    If the PRN is not availale, you should say "PRN Not Found".
    If 3033 is not in PRN It means PRN is not valid.
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



#Loading the model
def load_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.6)
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
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/text-embedding-004")
    
    # Loading saved vectors from local path
    db = FAISS.load_local(DB_FAISS_PATH, embeddings,allow_dangerous_deserialization=True)
    docs = db.similarity_search(user_question)
    
    chain = get_conversational_chain()
    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    return response




# suggetion ( chat histroy state is not there)
# change prompt template to get more better results
# if question is not related to university then send (please ask question related to university)
# Currently i testing this locally with ngrok, after getting the appropriate results i will deploy it on cloud, and also integrate with whatsapp.

