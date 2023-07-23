from langchain.llms import OpenAI
import streamlit as st

st.title("Quickstart App")
openai_api_key=st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    llm=OpenAI(temperature=0.7,openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form('Question_form'):
    input_text=st.text_area('Enter Text:','Ask your question here')
    submitted=st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(input_text)
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter OpenAI api key')