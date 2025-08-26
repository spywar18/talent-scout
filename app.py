# hiring-assistant/app.py

import streamlit as st
from chatbot import HiringAssistantChatbot
from utils import load_api_key
import os
import time

def main():
    """
    Main function to run the Streamlit hiring assistant application.
    """
    # --- Load API key ---
    try:
        api_key = load_api_key()
        os.environ["GOOGLE_API_KEY"] = api_key
    except ValueError as e:
        st.error(e)
        return

    # --- Streamlit UI Configuration ---
    st.set_page_config(
        page_title="TalentScout Hiring Assistant",
        page_icon="🤖",
        layout="centered"
    )

    st.title("🤖 TalentScout Hiring Assistant")
    st.markdown("Welcome! I'm here to help with the initial screening process.")

    # --- Session State Initialization ---
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = HiringAssistantChatbot()
        # Add initial greeting
        initial_greeting = st.session_state.chatbot.get_initial_greeting()
        st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

    # --- Display Chat History ---
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                st.session_state.chatbot.render_markdown_with_code(message["content"], st)
            else:
                st.markdown(message["content"])

    # --- User Input Handling ---
    if prompt := st.chat_input("Your response..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant's response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            try:
                assistant_response = st.session_state.chatbot.get_response(prompt)

                # Simulate streaming effect while building the response
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.03)  # slightly faster than before
                    # For streaming, show partial text
                    message_placeholder.markdown(full_response + "▌")

                # After streaming, render properly with Markdown + code highlighting
                message_placeholder.empty()  # clear placeholder
                st.session_state.chatbot.render_markdown_with_code(full_response, st)

            except Exception as e:
                st.error(f"An error occurred: {e}")
                full_response = "⚠️ Sorry, I encountered an error. Please try again."
                st.markdown(full_response)

        # Save assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
