from logger import Logger
from datetime import datetime
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
        AppState.scheduler.run(True)

    def store_trading_instruments(self, trading_instruments):
        (trading_instrument_types, trading_instrument_asset_classes) = self.get_trading_instruments_asset_classes(trading_instruments)
        log.info("Instruments", count=len(trading_instruments))
        self.put('trading_instruments', trading_instruments)
        self.put('trading_instrument_types', trading_instrument_types)
        self.put('trading_instrument_asset_classes', trading_instrument_asset_classes)
        self.put('trading_instruments_date', datetime.utcnow().date())

    def get_trading_instruments_asset_classes(self, trading_instruments):
        trading_instrument_types = {}
        trading_instrument_asset_classes = {}

        for instrument in trading_instruments:
            instrument_type = instrument['type']
            if instrument_type not in trading_instrument_types:
                trading_instrument_types[instrument_type] = []
            trading_instrument_types[instrument_type].append(instrument)
            
            asset_class = instrument['tags'][0]['name']
            if asset_class not in trading_instrument_asset_classes:
                trading_instrument_asset_classes[asset_class] = []
            trading_instrument_asset_classes[asset_class].append(instrument)
        
        return (trading_instrument_types, trading_instrument_asset_classes)

def heartbeat_task():
    while True:
        log.debug('Heartbeat')
        time.sleep(1.67)