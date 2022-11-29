from flask_app import app
from logger import Logger

log = Logger()

@app.route('/')
def root_get():
    """Path: / (Application root)"""
    return "OK", 200