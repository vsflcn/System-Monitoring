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

# Run the script when the container launches
CMD ["python", "./analysis.py"]
