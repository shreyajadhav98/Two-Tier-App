# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the complete application
COPY app/ .

# Expose Flask port
EXPOSE 5000

# Start Flask
CMD ["python", "app.py"]