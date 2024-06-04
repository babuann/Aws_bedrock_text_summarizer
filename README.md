# Aws_bedrock_text_summarizer
 This project demonstrates a full-stack application with a Serverless backend and dynamic frontend for real-time text processing. The backend uses AWS Lambda with Python, integrating Bedrock and Cohere Foundation Model for LLM responses. The frontend is built with Python, Docker, and Streamlit, making API calls to display streaming text responses.


 ### Backend
- **Technology**: AWS Lambda (Serverless)
- **Functionality**: Available as a Lambda Function URL.
- **Integration**: Uses Python to connect with Bedrock for generating responses from the Cohere Foundation Model.

### Frontend
- **Technology**: Python, Docker, Streamlit
- **Functionality**:
  - Users enter text via a Streamlit interface.
  - Sends an API call to the Lambda function URL with the input text.
  - Displays the response from the Lambda function as streaming text.
