#Pull base image
FROM python:3

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=3

#Set work directory
WORKDIR /app/backend

#Install dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

#Copy project
COPY . /app/backend/
