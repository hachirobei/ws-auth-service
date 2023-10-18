# docker/Dockerfile

# Use the official Python base image
FROM python:3.12

LABEL maintainer="Muhammad Hafizoddin <hachirobei93@gmail.com>"

# Set the working directory inside the container
WORKDIR /usr/src/app

# Set the PYTHONPATH
ENV PYTHONPATH=/usr/src/app:$PYTHONPATH

# Copy the requirements.txt from the docker/python folder into the container
COPY ./docker_ws/python/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application and its .env file into the container
COPY . /usr/src/app/

# Expose port 80 for Uvicorn
EXPOSE 80

# Set the module name for Uvicorn to run
ENV MODULE_NAME=main

# Command to run the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]