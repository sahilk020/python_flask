from flask import Flask
import os
import logging

app = Flask(__name__)

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'defaultsecret')
app.config['SECRET_KEY'] = SECRET_KEY

log_dir = '/var/log/flask'
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, 'app.log')

# Explicit file handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

# Add handler to Flask logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

app.logger.info("✅ Flask app is starting...")

@app.route('/')
def home():
    app.logger.info("Accessed / route")
    return f"✅ Hello from Flask! Secret key is: {SECRET_KEY}"

@app.route('/health')
def health():
    app.logger.info("Health check OK")
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
