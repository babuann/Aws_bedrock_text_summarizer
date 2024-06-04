import streamlit as st 
import json
import time
import requests

api_endpoint="function_url from aws_lambda"
def get_response(text):
    payload={
        "prompt":f"""Summaraize the information added .donot add any extra information {text}"""
    }
    response=requests.post(api_endpoint,json=payload)
    print(f"response status::{response.status_code}")
    response_text=response.text
    for word in response_text.split():
        yield word+" "
        time.sleep(0.1)

def main():
    
    st.set_page_config("Text Summarization Demo")
    st.header("AWS Bedrock integeration -Claude model")
    
    text=st.text_area("Text to summarize")
    
    if st.button("Summarize it"):
        with st.spinner("processing..."):
            st.write(get_response(text))
    
if __name__=="__main__":
    main()
