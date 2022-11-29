from logger import Logger

log = Logger()

class AppState(object):
    state = {}
    
    def __init__(self):
        AppState.state = {}

    def put(self, key, value):
        AppState.state[key] = value

    def get(self, key):
        return AppState.state[key] if key in AppState.state else None
