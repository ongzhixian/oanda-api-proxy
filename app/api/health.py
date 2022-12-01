# 
################################################################################
# Modules and functions import statements
################################################################################

from flask import request, make_response, abort
from flask_app import app
from logger import Logger

log = Logger()

@app.route('/api/health', methods=['GET', 'POST'])
def api_health():
    try:
        status_text = "OK"
        log.info("Health check", status=status_text)
        return status_text
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)
