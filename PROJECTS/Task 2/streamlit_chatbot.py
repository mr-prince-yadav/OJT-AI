import streamlit as st

st.set_page_config(page_title="Simple Chatbot", layout="centered")

st.title("🤖 Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Type a message...")

# Logic for response
def bot_response(user_msg):
    user_msg = user_msg.lower()
    if "hello" in user_msg or "hi" in user_msg:
        return "Hi there! How can I help you today?"
    elif "bye" in user_msg:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_msg:
        return "I'm just a bot, but I'm doing fine!"
    else:
        return "Sorry, I don't understand that."

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    response = bot_response(user_input)
    st.session_state.chat_history.append(("bot", response))

# Display chat history
for sender, msg in st.session_state.chat_history:
    with st.chat_message(sender):
        st.write(msg)
