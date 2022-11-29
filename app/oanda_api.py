
import json

from datetime import datetime
from glob import glob
from os import path, makedirs
from urllib.request import urlopen as url_open
from urllib.request import Request as url_request

from logger import Logger

log = Logger()

class OandaApi(object):
    def __init__(self, settings, output_path):
        self.account_id = settings['account_number']
        self.api_key = settings['api_key']
        self.rest_api_url = settings['rest_api_url']
        self.streaming_api_url = settings['streaming_api_url']
        self.output_path = output_path
        self.headers={
            'Authorization': f"Bearer {self.api_key}",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
        }
        required_sub_directories = [ 'instruments' ]
        for sub_directory in required_sub_directories:
            directory_path = path.join(self.output_path, sub_directory)
            full_path = path.abspath(directory_path)
            if not path.exists(full_path):
                try:
                    makedirs(full_path)
                except Exception:
                    log.error(f"ERROR - output path does not exists {full_path}")
                    exit(2)


    def save_data_to_file(self, data):
        FILE_DATETIME = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        FILE_NAME = f'instruments-{FILE_DATETIME}.txt'
        SAVE_FILE_PATH = path.join(self.output_path, 'instruments', FILE_NAME)
        with open(SAVE_FILE_PATH, 'w', encoding='utf-8') as out_file:
            out_file.write(data)
            log.info("Save instruments to file", file_name=FILE_NAME, file_path=SAVE_FILE_PATH)


    def get_account_instruments(self):
        """
        Get account instruments
        """
        account_id = self.account_id
        url = f"{self.rest_api_url}/v3/accounts/{account_id}/instruments"

        request = url_request(
            url, 
            data=None, 
            headers=self.headers
        )

        log.info("Fetching instruments", event="fetch instruments", status="start")
        with url_open(request) as response:
            response_data = response.read().decode("utf-8")
            log.info("Fetch instruments", event="fetch instruments", status="end")
            self.save_data_to_file(response_data)
        try:
            response_json = json.loads(response_data)
            return response_json['instruments'] if 'instruments' in response_json else []
        except Exception as ex:
            log.warn(f"Invalid response_json; {ex}")
            return []


    def current_instrument_file_exists(self):
        """
        Check if instrument file for current runtime date exists.
        Return tuple of 2 values:
        1. Exists  -- True / False
        2. FilePath / None
        """
        FILE_DATE = datetime.utcnow().strftime("%Y%m%d")
        glob_pattern = path.join(self.output_path, 'instruments', f'instruments-{FILE_DATE}*.txt')
        files = glob(glob_pattern)
        if len(files) <= 0:
            return (False, None)
        return (True, sorted(files)[-1])

    def get_instruments_from_file(self, file_path):
        """
        Read the instruments section of JSON file.
        """
        with open(file_path, 'r', encoding='utf-8') as in_file:
            log.info("Get instruments from file", file_path=file_path)
            response_json = json.loads(in_file.read())
            return response_json['instruments'] if 'instruments' in response_json else []

    def get_instruments(self):
        """
        Get instruments
        """

        (current_instrument_file_exists, file_path) = self.current_instrument_file_exists()

        if current_instrument_file_exists:
            return self.get_instruments_from_file(file_path)
        
        return self.get_account_instruments()