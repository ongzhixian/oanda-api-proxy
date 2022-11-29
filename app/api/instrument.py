# 
################################################################################
# Modules and functions import statements
################################################################################

import json
from flask import request, make_response, abort
from flask_app import app
from logger import Logger

log = Logger()

from main import app_state

@app.route('/api/instrument', methods=['GET', 'POST'])
def api_instrument():
    try:
        trading_instruments = app_state.get('trading_instruments')
        response_message = f"OK in instruments count: {len(trading_instruments)}"
        log.info(response_message)
        return json.dumps(trading_instruments)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)
