from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI()

st.header('Reasearch Tool')

user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)