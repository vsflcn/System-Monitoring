# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /home/ubuntu/Desktop

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure the Python script is executable
RUN chmod +x analysis.py

# Expose the port
EXPOSE 5000

#Command to run your Python script as a web server when the container launches
CMD ["python", "-m", "http.server", "5000"]
