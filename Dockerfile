# Use the official Python image for amd64 architecture.
# https://hub.docker.com/_/python
FROM python:3.12-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install any needed packages specified in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container.
EXPOSE 8000

# Define environment variable.
ENV NAME World

# Run the application.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
