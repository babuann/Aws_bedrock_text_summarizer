FROM python:3.11
EXPOSE 8082
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt 
COPY . /app
ENTRYPOINT [ "streamlit", "run", "app.py","--server.port=8082"]
