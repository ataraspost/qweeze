FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /qweeze/
RUN pip install -r requirements.txt
ADD . /qweeze/
