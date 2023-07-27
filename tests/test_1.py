import unittest

import time
import sys
import logging
from datetime import datetime

sys.path.insert(0, '/home/iwan/GITHUB/PY/currency_monitoring/src')
from config import API_KEY
from currencies_names import list_of_currencies


import tabulate
import pytz
import ast
import requests
from rich.console import Console
from bs4 import BeautifulSoup
import dearpygui.dearpygui as dpg

console = Console()

def close_program_with_error(name_of_error: str) -> str:
    # logger.error(name_of_error)
    console.print(f'{name_of_error}\nPlease reboot program!')


def query_execution() -> float:
    '''
    This function sends a request to the server
    and parses data from it: currency value
    '''

    first_currency = 'RUB'
    second_currency = 'USD'

    try:
        site_url = 'https://api.freecurrencyapi.com/v1/latest'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}

        full_page = requests.get(
            site_url,
            params={
                'apikey': API_KEY,
                'base_currency': first_currency,
                'currencies': second_currency},
            headers=headers)

    except requests.exceptions as err:
        # logger.error(err)
        return SystemExit(err)

    if full_page.status_code == 200:
        soup = BeautifulSoup(full_page.content, 'html.parser')
        soup_text = soup.getText()
        text = ast.literal_eval(soup_text)
        data = dict(text)['data']
        return list(data.values())[0]

    # logger.exception('Server don`t working')
    return  close_program_with_error('Sorry, server don`t working')

class Test(unittest.TestCase):

    def test_request(self):
        res = query_execution()
        self.assertIsInstance(res, float)


if __name__ == '__main__':
    unittest.main()

