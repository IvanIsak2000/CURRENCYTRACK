import requests
from bs4 import BeautifulSoup
import time
import re
import sys
import logging
from datetime import datetime

import tabulate
import pytz
import ast


def close_programm():
    print("INPUT ERROR")
    to_exit = input("PRESS ENTER FOR EXIT")
    exit()


try:
    from config import API_KEY as API_KEY
    
except:
    print('API_KEY is now found or not set!')
    close_programm()

logging.basicConfig(
    level=logging.INFO,
    filename="log_currency.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")


check_time = int(input("Время проверки/check time(сек/sec): "))
list_of_currencies = [
    'BCH',
    'BTC',
    'BTG',
    'BYN',
    'CAD',
    'CHF',
    'CNY',
    'ETH',
    'EUR',
    'GBP',
    'GEL',
    'IDR',
    'JPY',
    'LKR',
    'MDL',
    'MMK',
    'RSD',
    'RUB',
    'THB',
    'USD',
    'XRP',
    'ZEC']


first_currency = input(
    f"Введите первую валюту/Wtire first  currency: {list_of_currencies}): ")

second_currency = input(
    f"Введите вторую валюту/Wtire second  currency: {list_of_currencies}: ")

if first_currency and second_currency in list_of_currencies and first_currency != second_currency:
    pass
else:

    close_programm()

print(f"SETTINGS: 1 {first_currency} = {second_currency}")


def currency_checking(operation_number):

    # СБОР НЫНЕШНЕГО КУРСА ВАЛЮТ
    URL = (
        f'https://currate.ru/api/?get=rates&pairs={first_currency}{second_currency}&key={API_KEY}')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
    full_page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    soup_text = soup.getText()
    soup_dict = ast.literal_eval(soup_text)
    data = soup_dict["data"][first_currency + second_currency]
    return data


operation_number = 0

while True:

    try:

        currency_at_the_beginning = currency_checking(
            operation_number)  # first data
        current_time1 = datetime.now(pytz.timezone(
            'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")  # first time

        time.sleep(check_time)  # waiting

        currency_after = currency_checking(
            operation_number)  # second data
        current_time2 = datetime.now(pytz.timezone(
            'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")  # second time

        different = float(currency_at_the_beginning) - float(currency_after)
        print(operation_number)
        print(tabulate.tabulate([["Was",
                                  currency_at_the_beginning,
                                  current_time1,

                                  'OK'],
                                 ["Became",
                                  currency_after,
                                  current_time2,
                                  different]],
                                tablefmt="simple",
                                disable_numparse=False))

        with open('history_currency.txt', 'a') as file:
            data = tabulate.tabulate([["Was",
                                       currency_at_the_beginning,
                                       current_time1, 'OK'],
                                      ["Became",
                                     currency_after,
                                     current_time2, different]],
                                     tablefmt="simple",
                                     disable_numparse=False)

            file.write(f'{operation_number}')
            file.write(data)
            file.write('-----------------------------------------')

        # logging if OK
        logging.info(f'OK, operation  number:{operation_number}')

    except Exception as err:
        print('Error')
        logging.exception(err, exc_info=True)  # logging if  NOT OK
        pass

    operation_number += 1
