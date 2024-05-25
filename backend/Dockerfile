# FROM python:3.13.0a6-alpine3.18 as build_stage
FROM python:3.8.19-slim-bullseye AS build_stage

WORKDIR /flask-react-app-backend/

COPY . .

RUN apt update \ 
  && apt install -y --no-install-recommends build-essential curl libpq-dev \
  && apt clean

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "4","--bind", "0.0.0.0:8000", "main:app"]






