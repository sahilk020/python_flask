from flask import Flask
import os
import logging

app = Flask(__name__)

# Load secret from environment variable or fallback
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'defaultsecret')
app.config['SECRET_KEY'] = SECRET_KEY

# Create log directory if it doesn't exist
log_dir = '/var/log/flask'
os.makedirs(log_dir, exist_ok=True)

# Configure logging to file
log_file = os.path.join(log_dir, 'app.log')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)

# Log app start
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
