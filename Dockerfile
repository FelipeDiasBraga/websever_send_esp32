FROM python:3.9


RUN apt-get update && apt-get install -y python3-pip

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

WORKDIR /websever_send_esp32

CMD ["python3", "-u", "/main.py"]

