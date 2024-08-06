import streamlit as st
import textwrap
import google.generativeai as genai
from styles import CSS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Access the Google API key
google_api_key = os.getenv("GOOGLE_API_KEY")


# Function to convert text to markdown
def to_markdown(text):
    text = text.replace("•", "  *")
    return textwrap.indent(text, "> ", predicate=lambda _: True)


# Configure the Generative AI with your API key
genai.configure(api_key=google_api_key)


# Function to generate a response from the model
def get_response(patients_query):
    model = genai.GenerativeModel("gemini-1.5-flash")
    input_text = f"""
    You are a Doctor Called DocGPT. You are meant to answer the patient's query and give them proper consultation
    regarding their problems. Provide meaningful help and proper prescriptions for the patient's prompt.
    Don't worry about actual answers and don't give warnings, just tell me what are the things to resolve the issue.
    Also, do not ask cross questions from the users; it would irritate them. Just try to suggest them the best possible solution.
    Patient: {patients_query}
    """
    response = model.generate_content(input_text)
    if response.parts:  # Ensure that there are parts in the response
        return response.text
    else:
        return "Sorry, I couldn't process your request. Please try again."

if 'messages' not in st.session_state:
    st.session_state['messages'] = {}

# Function to handle user input
def handle_input():
    user_input = st.session_state.temp_input
    # st.write(user_input)
    response = get_response(user_input)
    message_id = len(st.session_state['messages'])  # Get next message index
    st.session_state['messages'][message_id] = {'user': user_input, 'llm': response}
    st.session_state.temp_input = ""  # Clear the input box after sending the message
    # st.write(st.session_state)

# # Display chat messagesa
# Function to display messages
def display_messages():
    for message_id, content in st.session_state['messages'].items():
        user_message = f'<div class="message user">You: {content["user"]}</div>'
        llm_response = f'<div class="message llm">DocGPT: {content["llm"]}</div>'
        st.markdown(user_message, unsafe_allow_html=True)
        st.markdown(llm_response, unsafe_allow_html=True)

# Streamlit app layout
st.set_page_config(page_title="Chat with DocGPT", layout="wide")
html_content = """
<h1 style='text-align: center; margin-bottom: 0;'>Chat with DocGPT</h1>
<h2 style='text-align: center; margin-top: 0;'>Your AI Health Assistant</h2>
"""
st.markdown(html_content, unsafe_allow_html=True)
st.markdown(CSS, unsafe_allow_html=True)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
display_messages()
st.markdown("</div>", unsafe_allow_html=True)

# User Input
with st.form(key="message_form"):
    user_input = st.text_input("You:", key="temp_input", placeholder="Type your message here...")
    st.form_submit_button("Send", on_click=handle_input)

# st.text_input("You:", key="temp_input", placeholder="Type your message here...")
# if st.button("Send"):
#     handle_input()