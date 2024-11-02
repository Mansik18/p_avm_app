FROM python:3.8-slim
#FROM pytorch/pytorch:2.4.1-cuda11.8-cudnn9-devel

WORKDIR /app

COPY ../.. /app

RUN pip install notebook
RUN pip install "fastapi[standard]" celery Redis flower

RUN apt-get update && apt-get install -y openssh-client

RUN mkdir -p /root/.ssh
COPY player /root/.ssh/id_rsa
COPY config /root/.ssh/config
RUN chmod 600 /root/.ssh/id_rsa

EXPOSE 8000
