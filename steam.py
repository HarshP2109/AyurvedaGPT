from retreivalFaiss import user_input
import streamlit as st
from quiz import Quiz
import time
import os



# Simulate a function that generates a response with a delay
def generate_response(user_message,key):
    # dbpath = 'db_ayurveda'
    response = user_input(user_message,key)
    
    time.sleep(2)  # Simulating a delay for response generation
    return f" {response}"



# Below Frontend

if __name__ == '__main__':

    # Initialize session state for API key and messages
    # if 'api_key' not in st.session_state:
    #     # st.session_state.api_key = st.secrets["gemini_key"]
    if 'Rag' not in st.session_state:
        st.session_state.Rag = []
    # if 'new' not in st.session_state:
    #     st.session_state.new = False
    if 'page' not in st.session_state:
        st.session_state.page = "Home"

    # Function to display chat interface
    def chat_interface():

        # Display chat history
        for chat in st.session_state.Rag:
            if chat["role"] == "user":
                with st.chat_message("user"):
                    st.markdown(f"**You:** {chat['content']}")
            else:
                with st.chat_message("assistant"):
                    st.markdown(f"**Assistant:** {chat['content']}")

        # Accept user input
        prompt = st.chat_input("Say something")

        if prompt:

            # Add user message to chat history
            st.session_state.Rag.append({"role": "user", "content": prompt})

            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(f"**You:** {prompt}")

            # Display loading message
            loading_message_placeholder = st.empty()
            loading_message_placeholder.markdown("**Loading...**")

            # Display assistant response in chat message container
            with st.chat_message("assistant"):

                key = st.secrets["gemini_key"]
                response = generate_response(prompt, key)
                st.markdown(f"**Assistant:** {response}")

            # Clear loading message and display response
            loading_message_placeholder.empty()
            st.session_state.Rag.append({"role": "assistant", "content": response})

        # st.write(messages_key)

    # Main application
    st.set_page_config(page_title="Ayurveda GPT App", layout="wide")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Go to", ["Home", "Ayurveda Chat", "Prakriti"])

    if page == "Home":
        st.title("Home Page")
        st.markdown("""
            ## Welcome to the Ayurveda GPT App!

            This Webapp helps you with Ayurvedic Knowledge. You can ask any question to it, 
            and it will answer using the Gemini API with Faiss databases.

            ### How to Use
            1. Navigate to Prakriti and answer some questions to know your prakriti.       
            2. Navigate to the Ayurveda GPT page using the sidebar.
            3. Start interacting with the system.

            ### Workflow
            Below is a flowchart demonstrating how it works:

        """, unsafe_allow_html=True)
        st.image('Flowchart\AyurvedaGPT.png', caption='Ayurveda GPT Flowchart')


        st.session_state.api_key = ""
        st.session_state.page = "Home"

    elif page == "Ayurveda Chat":
        st.title("Ayurveda GPT")
        st.session_state.page = "Rag"
        # st.session_state.new = False
        chat_interface()

    elif page == "Prakriti":
        st.session_state.page = "Rag"
        # st.session_state.new = False
        Quiz()



        