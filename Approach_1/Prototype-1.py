import google.generativeai as palm
import os
import streamlit as st
import streamlit_chat as cht
from PyPDF2 import PdfReader
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']['api_key']

PAGE_TITLE = "PalmLangBot"  # PalM + LangChain
SETTINGS_TITLE = "Settings"
UPLOAD_INSTRUCTIONS = "Upload your PDF Files and Click on the Process Button"
PROCESS_BUTTON_LABEL = "Process"





def is_university_related(text):
    university_keywords = ['university', 'college', 'education', 'academic', 'degree']
    return any(keyword in text.lower() for keyword in university_keywords)

def has_university_mention_in_history():
    if st.session_state.chatHistory:
        for message in st.session_state.chatHistory:
            if is_university_related(message.content):
                return True
    return False




def get_conversational_chain(vector_store):
    llm = GooglePalm()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(),
                                                                memory=memory)
    return conversation_chain

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GooglePalmEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

def Processing_data(pdf_docs):
    with st.spinner("Processing"):
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        vector_store = get_vector_store(text_chunks)
        st.session_state.conversation = get_conversational_chain(vector_store)

def user_input(user_question):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})

        if 'chat_history' in response:
            st.session_state.chatHistory = response['chat_history']
            for i, message in enumerate(st.session_state.chatHistory):
                key = f"chat_widget_{i}"  # Generate a unique key for each chat widget
                if i % 2 == 0:
                    cht.message(f"Human: {message.content}", is_user=True, key=key)
                else:
                    cht.message(f"Bot: {message.content}", key=key)
        else:
            st.write("Error: Unexpected response from LangChain.")
    else:
        st.write("Error: LangChain conversation not initialized.")


def main():
    st.set_page_config(PAGE_TITLE)
    st.header(PAGE_TITLE + "💬")

    user_question = st.chat_input("Ask a Question from the PDF Files")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title(SETTINGS_TITLE)
        st.subheader("Upload Your Documents")

        pdf_docs = st.file_uploader(UPLOAD_INSTRUCTIONS, accept_multiple_files=True)
        if st.button(PROCESS_BUTTON_LABEL):
            Processing_data(pdf_docs)
            st.success("Done")


if __name__ == "__main__":
    main()
