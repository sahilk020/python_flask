FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy your application code
COPY app.py /app/

# Create log directory (used by Promtail sidecar)
RUN mkdir -p /var/log/flask

# Install Flask
RUN pip install flask

# Expose port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
