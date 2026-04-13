import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_classic.agents import create_react_agent,AgentExecutor
from langsmith import Client
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_core.prompts import PromptTemplate



st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/shubh9165/SearchGPT-Agent](https://github.com/shubh9165/SearchGPT-Agent).
"""


arxiv_api_wrapper=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
arxiv=ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

wiki_api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki=WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

search=DuckDuckGoSearchRun(name="search")

st.sidebar.title("Settings")

api_key=st.sidebar.text_input("Enter your groq api key",type="password")


if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistent","content":"hey i am ai assistent,how i can help you"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="Hey,how are you"):
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(
        groq_api_key=api_key,
        model="llama-3.3-70b-versatile",
        temperature=0,
        streaming=True,
    )
    tools=[search,wiki,arxiv]

    qa_prompt = PromptTemplate.from_template("""
    You are a helpful AI assistant.

    You have access to the following tools:
    {tools}

    Tool names: {tool_names}

    Use the following format:

    Question: {input}
    Thought: think step by step
    Action: one of [{tool_names}]
    Action Input: input to the tool
    Observation: result of the tool
    ... (repeat Thought/Action/Observation as needed)
    Thought: I now know the final answer
    Final Answer: answer to the question

    {agent_scratchpad}
    """)


    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=qa_prompt
    )

    search_agent = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        early_stopping_method="force",
        handle_parsing_errors=True
    )

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = search_agent.invoke(
            {"input": prompt},
            {"callbacks": [st_cb]}
        )

        st.session_state.messages.append({'role':'assistant',"content":response})
        st.write(response)




