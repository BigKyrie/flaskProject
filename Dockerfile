FROM python:3.8

ADD . /Project1/

WORKDIR /Project1

RUN  pip install -r /Project1/requirements.txt

CMD python3.8 app.py
