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

from main import query_execution

class Test(unittest.TestCase):

    def test_correct_request(self):
        res = query_execution('RUB', 'USD')
        self.assertIsInstance(res, float)

if __name__ == '__main__':
    unittest.main()

