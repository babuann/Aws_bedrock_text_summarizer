import streamlit as st 
import json
import time
import requests

api_endpoint="function_url from aws_lambda"
def get_response(text):
    payload={
        "prompt":f"""generate an accurate summary in the following format:

Projects:

[List of projects]


Morning:

[Activities during the morning]


Mid-Morning:

[Activities during the mid-morning]


Noon:

[Activities during noon]


Afternoon:

[Activities during the afternoon]


Main Topics Discussed:

[List of main topics discussed]



The summary should include the people you interacted with, the topics discussed, and the associated projects. Keep the summary concise, using less than 200 words. The purpose is to help the team leader, client, or boss quickly understand what you have been working on during the captured period\n {text}"""
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
