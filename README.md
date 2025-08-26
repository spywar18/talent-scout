# TalentScout - AI Hiring Assistant Chatbot

## 1. Project Overview

This project is an intelligent **Hiring Assistant Chatbot** developed for "TalentScout," a fictional recruitment agency. The chatbot is designed to automate and enhance the initial screening process for technology job candidates. It interacts with candidates through a clean, web-based interface, gathers essential information, and conducts a dynamic technical assessment based on their declared technology stack.

The application is built with Python and Streamlit and is powered by Google's Gemini Pro for its core conversational AI. It also includes advanced features like sentiment analysis and multilingual support to create a more empathetic and accessible candidate experience.

### Live Demo

**You can interact with the live application here:** [https://hiring-assistant-554647416942.us-central1.run.app/](https://hiring-assistant-554647416942.us-central1.run.app/)

## 2. Technical Details

* **Programming Language**: Python 3.11
* **Frontend UI**: Streamlit
* **Large Language Model (LLM)**: Google Gemini 1.5 Flash
* **Key Libraries**:
  * `streamlit` – For building the interactive web interface
  * `google-generativeai` – Official Python SDK for Gemini API
  * `google-cloud-language` – For sentiment analysis
  * `python-dotenv` – For managing environment variables securely

### Architecture

The application is structured into three main components:

1. **`app.py`** – Main Streamlit application handling UI, session management, and custom styling.
2. **`chatbot.py`** – Contains `HiringAssistantChatbot` class, manages conversation logic, prompt engineering, and interactions with Google Gemini & Natural Language APIs.
3. **`utils.py`** – Utility module for helper functions like loading environment variables.

## 3. Prompt Design

The chatbot relies on a detailed system prompt provided to Gemini, located in `chatbot.py`. The prompt defines the bot's persona, workflow, and rules for conversation handling.

**Key Aspects:**

* **Persona Definition** – Friendly, empathetic, professional assistant.
* **Structured Workflow** – Multi-phase conversation flow: info gathering → technical assessment → evaluation.
* **Rich Formatting Instructions** – Use Markdown for headings, bold text, code blocks, and lists.
* **Advanced Feature Integration** – Sentiment and language awareness to adapt tone.
* **Strict Guardrails** – Prevent the chatbot from revealing instructions and handle unclear input gracefully.

## 4. Challenges and Solutions

* **Challenge:** Initial chatbot responses were raw text and hard to read.  
  **Solution:** Enhanced prompt with Markdown formatting for better UI rendering.

* **Challenge:** Bot occasionally revealed internal instructions.  
  **Solution:** Added "Critical Rules of Behavior" to handle unclear input politely.

* **Challenge:** Streamlit UI theme clashed with custom styling.  
  **Solution:** Added custom CSS in `app.py` for light theme and high-contrast text.

## 5. Installation Instructions

### Prerequisites

* Python 3.9+
* Google Cloud Platform (GCP) account with billing enabled
* Google API Key with Gemini and Natural Language APIs enabled

### Step-by-Step Guide

**1. Clone the Repository:**
```
git clone <your-repository-url>
cd hiring-assistant

```

**2. Create a Virtual Environment:**

### Windows
```
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies:**

```
pip install -r requirements.txt
```


**4. Set Up Your API Key:**
Create a .env file in the root directory:
```
GOOGLE_API_KEY="your-google-api-key"

```
**5. Run the Application:**

```
streamlit run app.py
```

**6. Deployment Guide (Google Cloud Run)**
```
1. Create a Dockerfile
dockerfile
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501

# Define the command to run your app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
```

2. Create a Procfile
```
web: streamlit run app.py
```

4. Deploy
```
gcloud run deploy hiring-assistant \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```
After deployment, the command outputs a Service URL — your live link.