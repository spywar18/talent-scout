# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Expose the port Cloud Run expects
EXPOSE 8080

# Use shell form of CMD so $PORT is expanded
CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.enableCORS=false