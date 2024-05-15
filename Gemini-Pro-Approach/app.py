import streamlit as st
from main import user_input
st.set_page_config(
    page_title="Inquiry Chatbot",
    page_icon="🤖"

)

def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to the Inquiry Chatbot! Please enter your inquiry below and I will do my best to help you out."}]

def main():
    st.title("Inquiry Chatbot")
    st.write("Welcome to the Inquiry Chatbot! Please enter your inquiry below and I will do my best to help you out.")
    st.sidebar.button('clear chat',on_click=clear_chat_history)


    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "Welcome to the Inquiry Chatbot! Please enter your inquiry below and I will do my best to help you out."}]
        
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])

        
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Display chat messages and bot response
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = user_input(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response['output_text']:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        if response is not None:
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)

if __name__ == "__main__":
    main()