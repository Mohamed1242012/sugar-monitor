# Use a minimal base image with Python
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

EXPOSE 5000

# Use Gunicorn for production WSGI serving
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
