FROM python:3.9

WORKDIR /app

# Copy Python code
COPY app.py .

# ✅ Copy your templates folder (critical for Flask)
COPY templates/ templates/

# Install dependencies
RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
