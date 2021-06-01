# Dockerfile for a Python App
FROM python:3.8
WORKDIR /name-api
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
