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
        response_message = "OK"
        log.info("response_message")
        return response_message
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)
