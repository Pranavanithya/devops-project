import logging
from flask import Flask

app = Flask(__name__)

# Configure logging to a file
logging.basicConfig(filename='flask_logs.log', level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info("Hello route was accessed")
    return "Hello from Flask"

