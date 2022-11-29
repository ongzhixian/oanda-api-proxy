import os
import json
import logging
import threading

from datetime import datetime
from os import path
from urllib.parse import quote
from urllib.request import urlopen as url_open
from urllib.request import Request as url_request

import pika

from logger import setup_logging, Logger
from oanda_api import OandaApi
from flask_app import app
from app_state import AppState, heartbeat_task
from data_refresh_tasks import instruments_refresh_task

app_state = AppState()

def get_configuration_settings():
    with open("app-settings.json", "r", encoding="utf-8") as in_file:
        return json.loads(in_file.read())

def get_oanda_settings(configuration_settings):
    if "USERPROFILE" not in os.environ:
        return None
    
    user_profile_path = os.environ["USERPROFILE"]

    if 'secret_configuration_files' not in configuration_settings or 'oanda' not in configuration_settings['secret_configuration_files']:
        return None
    
    oanda_settings_path = configuration_settings['secret_configuration_files']['oanda']
    
    oanda_settings_full_path = path.join(user_profile_path, oanda_settings_path)

    if not path.exists(oanda_settings_full_path):
        return None

    with open(oanda_settings_full_path, "r", encoding="utf-8") as in_file:
        return json.loads(in_file.read())

def get_output_path():
    if "USERPROFILE" not in os.environ:
        return path.join(os.getcwd(), "temp")
    
    user_profile_path = os.environ["USERPROFILE"]
    
    return path.join(user_profile_path, "Dropbox\\myThinkBook\\oanda")
    
if __name__ == "__main__":

    configuration_settings = get_configuration_settings()

    oanda_settings = get_oanda_settings(configuration_settings)

    output_path = get_output_path()

    log = setup_logging()

    # (url_parameters, database_settings, oanda_settings, output_path) = get_settings_from_arguments()
    
    oanda_api = OandaApi(oanda_settings, output_path)

    trading_instruments = oanda_api.get_instruments()

    app_state.store_trading_instruments(trading_instruments)

    
    
    # store_account_instruments_to_database(trading_instruments)
    # instrument_code_list = get_instrument_code_list(trading_instruments)
    # publish_tickers(url_parameters, instrument_code_list)

    # instruments_refresh_thread = threading.Thread(target=instruments_refresh_task, args=(1,), daemon=True)
    # instruments_refresh_thread.start()

    # app_state.schedule(3, instruments_refresh_task, ("3sec",))
    # app_state.schedule(5, instruments_refresh_task, ("5sec",))
    # app_state.schedule(8, instruments_refresh_task, ("8sec",))
    # app_state.schedule(8, instruments_refresh_task, ("8sec",))

    # heartbeat_thread = threading.Thread(target=heartbeat_task, daemon=True)
    # heartbeat_thread.start()

    app.run(host='0.0.0.0', port=31000, debug=False)
    log.info("Program complete", source="program", event="complete")
