# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x analysis.py

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "analysis.py"]
