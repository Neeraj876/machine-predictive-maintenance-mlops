FROM python:3.8-slim-buster
WORKDIR /DIR
COPY . /app

RUN apt update -y && apt install awscli -y

RUN pip3 install -r requirements.txt

CMD ["python3", "application.py"]