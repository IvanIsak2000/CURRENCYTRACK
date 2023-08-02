import unittest

import time
import sys
import logging
from datetime import datetime

sys.path.insert(0, '/home/iwan/GITHUB/PY/CURRENCYTRACK/src')
from config import API_KEY
from currencies_names import list_of_currencies
import tabulate
import pytz
import ast
import requests
from rich.console import Console
from bs4 import BeautifulSoup
# import dearpygui.dearpygui as dpg

console = Console()

from main import request_to_api_to_get_page, page_status_code_is_valid

class Test(unittest.TestCase):

    def test_correct_request(self):
        res = request_to_api_to_get_page('RUB', 'USD')
        self.assertIsInstance(res, tuple)

    def test_duplicate_currencies(self):
        res = request_to_api_to_get_page('USD', 'USD')
        self.assertIsInstance(res, tuple)

    def test_status_200(self):
        get_value_and_time =  request_to_api_to_get_page('RUB', 'EUR')
        status_200 = page_status_code_is_valid(get_value_and_time[0])
        self.assertEqual(status_200, True)
        
if __name__ == '__main__':
    unittest.main()

