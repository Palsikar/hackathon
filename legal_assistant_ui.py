import streamlit as st
import requests
import uuid

st.title("Legal AI Assistant")

# Generate unique user ID for conversation tracking
user_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.write("Ask a legal question, and the AI will guide you.")

for message in st.session_state.chat_history:
    st.text_area(message["role"], value=message["content"], height=100, disabled=True)

user_query = st.text_input("Your Question:")

if st.button("Send"):
    if user_query:
        response = requests.post("http://127.0.0.1:5000/chat", json={"user_id": user_id, "query": user_query})
        bot_reply = response.json()["response"]

        st.session_state.chat_history.append({"role": "You", "content": user_query})
        st.session_state.chat_history.append({"role": "Chatbot", "content": bot_reply})

        st.experimental_rerun()
