from flask import Flask, request, jsonify
import os
import logging
import time

app = Flask(__name__)

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'defaultsecret')
app.config['SECRET_KEY'] = SECRET_KEY

log_dir = '/var/log/flask'
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, 'app.log')

# Formatter for NGINX-style access logs
nginx_formatter = logging.Formatter('%(message)s')

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(nginx_formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(nginx_formatter)

# Add handlers to logger
app.logger.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request(response):
    duration = round((time.time() - request.start_time) * 1000, 2)  # in ms
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    method = request.method
    path = request.path
    status = response.status_code
    user_agent = request.headers.get('User-Agent', '-')
    log_line = f'{ip} - - [{time.strftime("%d/%b/%Y:%H:%M:%S +0000")}] "{method} {path} HTTP/1.1" {status} {duration}ms "{user_agent}"'
    app.logger.info(log_line)
    return response

@app.route('/')
def home():
    return jsonify(message=f"✅ Hello from Flask! Secret key is: {SECRET_KEY}")

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.logger.info("✅ Flask app is starting...")
    app.run(host='0.0.0.0', port=5000)
