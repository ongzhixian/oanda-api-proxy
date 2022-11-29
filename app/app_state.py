from logger import Logger

import sched, time

log = Logger()

class AppState(object):
    state = {}
    scheduler = sched.scheduler(time.time, time.sleep)
    
    def __init__(self):
        log.info("AppState init")

    def put(self, key, value):
        AppState.state[key] = value

    def get(self, key):
        return AppState.state[key] if key in AppState.state else None

    def schedule(self, action_time, action, *argument, **kwargs):
        AppState.scheduler.enterabs(action_time, priority=1, action=action, argument=argument, kwargs=kwargs)
        res = AppState.scheduler.run(True)
        breakpoint()