# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /home/ubuntu/Desktop

# Copy the Python script into the container
COPY analysis.py .

# Expose the port
EXPOSE 5000

#Command to run your Python script as a web server when the container launches
CMD ["python", "-m", "http.server", "5000"]
