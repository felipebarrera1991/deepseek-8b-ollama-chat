import streamlit as st
from langchain_ollama import ChatOllama

# Configure LLM
llm = ChatOllama(
    model="deepseek-r1:8B", 
    base_url='http://localhost:11434'
)

# Configure Streamlit
st.set_page_config(page_title="DeepSeek Chat", layout="centered")
st.title("Chat with DeepSeek!")

# Create message history
if "messages" not in st.session_state:
    st.session_state['messages'] = []
messages = st.session_state['messages']

# Display previous messages
for msg_type, content in messages:
    chat = st.chat_message(msg_type)
    chat.markdown(content)

# Get user input
prompt = st.chat_input('Send your message to DeepSeek...')

if prompt:
    messages.append(('human', prompt))

    # Display user's question
    chat = st.chat_message('human')
    chat.markdown(prompt)

    # Generate AI response
    response = llm.invoke(messages).content
    messages.append(('ai', response))

    # Display AI response
    chat = st.chat_message('ai')
    chat.markdown(response)
