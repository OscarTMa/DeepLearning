# Base image
FROM python:3.8-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# Copy app
COPY . .

# Expose the API port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
