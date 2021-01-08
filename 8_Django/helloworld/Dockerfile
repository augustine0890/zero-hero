# Pull base image
# FROM python:3.8-slim
FROM python:3.8.3-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
# WORKDIR /code
WORKDIR /usr/src/app

# Install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install dependencies
# COPY Pipfile Pipfile.lock /code/
# RUN pip install pipenv && pip install psycopg2-binary && pipenv install --system
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint.sh
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Copy project
COPY . .

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
