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


@app.route('/api/instrument/type/summary', methods=['GET', 'POST'])
def api_instrument_type_summary():
    try:
        trading_instrument_types = app_state.get('trading_instrument_types')

        summary = {}
        for type_name in trading_instrument_types:
            summary[type_name] = len(trading_instrument_types[type_name])

        return json.dumps(summary)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)


@app.route('/api/instrument/type/', methods=['GET', 'POST'])
def api_instrument_type_all():
    try:
        trading_instrument_types = app_state.get('trading_instrument_types')
        return json.dumps(trading_instrument_types)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)


@app.route('/api/instrument/type/<type_name>', methods=['GET', 'POST'])
def api_instrument_type(type_name):
    try:
        type_name = type_name.upper()
        trading_instrument_types = app_state.get('trading_instrument_types')
        result = trading_instrument_types[type_name] if type_name in trading_instrument_types else []

        return json.dumps(result)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)


@app.route('/api/instrument/asset-class/summary', methods=['GET', 'POST'])
def api_instrument_asset_class_summary():
    try:
        trading_instrument_asset_classes = app_state.get('trading_instrument_asset_classes')

        summary = {}
        for asset_class in trading_instrument_asset_classes:
            summary[asset_class] = len(trading_instrument_asset_classes[asset_class])

        return json.dumps(summary)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)


@app.route('/api/instrument/asset-class/', methods=['GET', 'POST'])
def api_instrument_asset_class_all():
    try:
        trading_instrument_asset_classes = app_state.get('trading_instrument_asset_classes')
        return json.dumps(trading_instrument_asset_classes)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)


@app.route('/api/instrument/asset-class/<class_name>', methods=['GET', 'POST'])
def api_instrument_asset_class(class_name):
    try:
        class_name = class_name.upper()
        trading_instrument_asset_classes = app_state.get('trading_instrument_asset_classes')
        result = trading_instrument_asset_classes[class_name] if class_name in trading_instrument_asset_classes else []

        return json.dumps(result)
    except Exception as e:
        log.info("ERROR----------ERROR----------")
        log.error(e)
