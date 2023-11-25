import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_host = os.environ.get("BACKEND_API_URI", "127.0.0.1")

# Streamlit UI elements
st.title("Data streaming for AI apps")

prompt = st.text_input("Search for recent events")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.sidebar.text(f"📩 {message['content']}")

    url = f"{api_host}"
    data = {"query": prompt, "user": "user"}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        response = response.json()
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error(
            f"Failed to send data to Discounts API. Status code: {response.status_code}"
        )