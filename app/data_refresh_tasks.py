import logging

import threading

import time
from datetime import datetime

def instruments_refresh_task(name):
    logging.info("Thread %s: starting %s", name, datetime.now())

    print("do something")

    time.sleep(2)
    
    print("something is done")

    logging.info("Thread %s: finishing %s", name, datetime.now())