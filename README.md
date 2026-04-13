# 🚀 SearchGPT Agent  
*A Tool-Augmented Intelligent AI Agent for Real-Time Knowledge Retrieval*

---

## 📌 Overview

**SearchGPT Agent** is an AI-powered chatbot built using **LangChain, Groq LLM, and Streamlit** that goes beyond traditional Q&A systems.

Unlike standard chatbots, this project implements a **ReAct (Reason + Act) Agent**, enabling it to:
- Think step-by-step  
- Decide when to use external tools  
- Fetch real-time information  
- Provide accurate and intelligent responses  

---

## 🧠 Key Features

- 🤖 **AI Agent (Not Just Chatbot)**  
  Uses reasoning + action-based architecture  

- 🌐 **Real-Time Web Search**  
  Integrated with DuckDuckGo  

- 📚 **Wikipedia Integration**  
  Fetches factual information  

- 📄 **Arxiv Research Access**  
  Retrieves academic paper summaries  

- 💬 **Interactive Chat UI**  
  Built with Streamlit  

- 🔍 **Transparent Reasoning**  
  Displays agent thoughts using callback handler  

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM:** Groq (LLaMA 3.3 70B)  
- **Framework:** LangChain  
- **Tools Integrated:**
  - DuckDuckGo Search  
  - Wikipedia API  
  - Arxiv API  

---

## 🔄 How It Works

The agent follows the **ReAct Framework**:
Question → Thought → Action → Observation → Final Answer


### Workflow:
1. User enters a query  
2. Agent analyzes the question  
3. Decides whether to:
   - Answer directly OR  
   - Use a tool (search, Wikipedia, Arxiv)  
4. Retrieves information  
5. Generates final response  

---

## 📂 Project Structure
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/shubh9165/SearchGPT-Agent.git
cd SearchGPT-Agent

### 2️⃣ Install dependencies
pip install -r requirements.txt

### 3️⃣ Run the application
streamlit run app.py

### 4️⃣ Add API Key
Enter your Groq API Key in the sidebar
