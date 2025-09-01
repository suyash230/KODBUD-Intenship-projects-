import streamlit as st
import datetime

def chatbot_response(user_input):
    """
    Generates a response based on a set of predefined rules.
    This function is the same core logic from our CLI chatbot.

    Args:
        user_input (str): The text entered by the user.

    Returns:
        str: The chatbot's response.
    """
    processed_input = user_input.lower().strip()

    if 'hello' in processed_input or 'hi' in processed_input or 'hey' in processed_input:
        return "Hello there! How can I help you today?"
    elif 'how are you' in processed_input:
        return "I'm just a bunch of code, but I'm doing great! Thanks for asking."
    elif 'your name' in processed_input or 'who are you' in processed_input:
        return "I am a simple rule-based chatbot, created to assist you."
    elif 'what can you do' in processed_input or 'help' in processed_input:
        return "I can answer some basic questions. Try asking me the time, about our company's location, or who made me."
    elif 'how does this company work' in processed_input or 'company location' in processed_input:
        return "Our company focuses on providing excellent solutions and innovative products to our clients. Our main office is located in New Delhi."
    elif 'time' in processed_input:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        return f"The current time is {current_time}."
    elif 'who made you' in processed_input or 'creator' in processed_input:
        return "I was created by a talented developer during their internship project!"
    elif 'weather' in processed_input:
        return "I can't check the weather, but I hear there's a great Python app for that! 😉"
    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Rule-Based Chatbot")
st.caption("A friendly chatbot to answer your questions.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello there! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = chatbot_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

