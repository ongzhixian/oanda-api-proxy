import logging

import threading

import time
from datetime import datetime

refresh_task_threads = []

def setup_threads():
    heartbeat_thread = threading.Thread(target=heartbeat_task, daemon=True)
    refresh_task_threads.append(heartbeat_thread)

def instruments_refresh_task(name):
    logging.info("Thread %s: starting %s", name, datetime.now())

    print("do something")

    time.sleep(2)
    
    print("something is done")

    logging.info("Thread %s: finishing %s", name, datetime.now())