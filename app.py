# importing the required libraries
from langchain.llms import OpenAI # to use openai api
from dotenv import load_dotenv # to load api keys that are present in .env files
import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

def get_openai_response(text,source,target):
    llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0)
    template="translate the {text} from the {source} language to the {target} language without displaying any extra words except the translation word"
    pormpt=PromptTemplate(input_variables=["text","source","target"],template=template)
    chain=LLMChain(llm=llm,prompt=pormpt)
    response=chain.predict(text=text,source=source,target=target)
    return response

st.set_page_config(page_title="The Universal Translator")

st.header("The Universal Translator")

text=st.text_input("enter the text you want to translate")
source=st.text_input("enter the language name in which you have written the text")
target=st.text_input("enter the language name to which you want to translate")


response=get_openai_response(text,source,target)

submit=st.button("translate")

## If ask button is clicked

if submit:
    st.write(response)