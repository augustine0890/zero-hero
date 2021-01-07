# Pull base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv && pip install psycopg2-binary && pipenv install --system

# Copy project
COPY . /code/