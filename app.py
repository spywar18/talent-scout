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
    # Load the API key and set it as an environment variable
    try:
        api_key = load_api_key()
        os.environ["GOOGLE_API_KEY"] = api_key
    except ValueError as e:
        st.error(e)
        st.stop()

    # --- UI Enhancements: Custom CSS for a Light Theme ---
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #f0f2f6 0%, #e9ecef 100%);
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .stChatMessage {
                background: #fff;
                border-radius: 16px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04);
                padding: 18px 22px;
                margin-bottom: 18px;
                max-width: 600px;
                font-size: 1.08rem;
                color: #222;
                border: none;
            }
            .st-emotion-cache-1v0mbdj > img {
                border-radius: 50%;
                box-shadow: 0 1px 4px rgba(0,0,0,0.08);
            }
            .stMarkdown, h1, h2, h3, p {
                color: #222 !important;
            }
            .stChatInputContainer {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 32px;
            }
            .stTextInput {
                border-radius: 12px !important;
                border: 1px solid #d1d5db !important;
                padding: 12px 16px !important;
                font-size: 1.08rem !important;
                background: #fff !important;
                box-shadow: 0 1px 4px rgba(0,0,0,0.04);
            }
            .stButton > button {
                border-radius: 12px !important;
                background: #0072ff !important;
                color: #fff !important;
                font-weight: 600 !important;
                padding: 10px 24px !important;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            }
        </style>
    """, unsafe_allow_html=True)

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
        initial_greeting = "Hello! I'm the intelligent hiring assistant. I'll be helping with the initial screening process today. To start, could you please tell me your full name?"
        st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

    # --- Display Chat History ---
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --- User Input Handling ---
    if prompt := st.chat_input("Your response..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # --- Response Handling ---
        with st.chat_message("assistant"):
            try:
                response = st.session_state.chatbot.get_response(prompt)
                if hasattr(response, '__iter__') and not isinstance(response, str):
                    # If response is a generator or stream, use st.write_stream
                    full_response = st.write_stream(response)
                else:
                    # If response is a string, use st.write
                    full_response = response
                    st.write(full_response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                full_response = "Sorry, I encountered an error. Please try again."
                st.markdown(full_response)

        # Add the complete assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
