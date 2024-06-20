from crew import crew_news
import streamlit as st
import os

## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## streamlit framework

st.title('News Report Generation')
input_text=st.text_input("Search the topic u want")

if st.button("Search") and input_text :
    result=crew_news.kickoff(inputs={'topic':input_text})
    st.write(result)