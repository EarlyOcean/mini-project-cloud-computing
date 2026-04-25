FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./api.py /app

#CMD python3 test.py
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
