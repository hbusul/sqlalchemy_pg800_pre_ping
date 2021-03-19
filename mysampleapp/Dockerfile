FROM python:3.7-buster

RUN pip install SQLAlchemy==1.3.5 pg8000==1.13.2

COPY main.py .

CMD python3 -u main.py