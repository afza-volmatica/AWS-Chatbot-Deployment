import streamlit as st
import requests

# Backend API URL
import os

API_URL = os.getenv(
    "API_URL",
    "http://backend:8000/chat"
)
st.set_page_config(
    page_title="Ollama Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Ollama Qwen Chatbot")
st.markdown("Ask anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_prompt = st.chat_input("Type your message...")

if user_prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Call backend
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "message": user_prompt
                    },
                    timeout=120
                )

                if response.status_code == 200:

                    bot_response = response.json()["response"]

                else:

                    bot_response = (
                        f"Backend Error: {response.status_code}"
                    )

            except Exception as e:

                bot_response = (
                    f"Connection Error: {str(e)}"
                )

            st.markdown(bot_response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_response
        }
    )