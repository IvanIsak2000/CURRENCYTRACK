import time
import re
import sys
import logging
from datetime import datetime

import tabulate
import pytz
import ast
import requests
from bs4 import BeautifulSoup
import dearpygui.dearpygui as dpg


def close_programm(name_of_error):
    print(name_of_error)
    to_exit = input("PRESS ENTER FOR EXIT")
    exit()

logging.basicConfig(
    level=logging.INFO,
    filename="log_currency.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")


list_of_currencies = [
    'AUD',
    'AZN',
    'GBP',
    'AMD',
    'BYN',
    'BGN',
    'BRL',
    'HUF',
    'VND',
    'HKD',
    'GEL',
    'DKK',
    'AED',
    'USD',
    'EUR',
    'EGP',
    'INR',
    'IDR',
    'KZT',
    'CAD',
    'QAR',
    'KGS',
    'CNY',
    'MDL',
    'NZD',
    'NOK',
    'PLN',
    'RON',
    'XDR',
    'SGD',
    'TJS',
    'THB',
    'TRY',
    'TMT',
    'UZS',
    'UAH',
    'CZK',
    'SEK',
    'CHF',
    'RSD',
    'ZAR',
    'KRW',
    'JPY']


def query_execution(operation_number):
    first_currency = dpg.get_value('currency_1')  # default RUB
    second_currency = dpg.get_value('currency_2')
    URL = (
        f'https://www.cbr-xml-daily.ru/daily_json.js')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
    full_page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    soup_text = soup.getText()
    soup_dict = ast.literal_eval(soup_text)
    data = soup_dict['Valute'][second_currency]['Value']
    return data


def main():
    first_currency = dpg.get_value('currency_1')  # default RUB
    second_currency = dpg.get_value('currency_2')
    check_time = round(float(dpg.get_value('check_time')))

    if first_currency == second_currency:
        error = 'Two identical currencies!'
        return close_programm(error)
    dpg.set_value('info', f"SETTINGS: 1 {first_currency} = {second_currency}")
    operation_number = 0
    while True:

        try:
            currency_at_the_beginning = query_execution(
                operation_number)  # first data
            current_time1 = datetime.now(pytz.timezone(
                'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")  # first time

            time.sleep(check_time)  # waiting

            currency_after = query_execution(
                operation_number)  # second data
            current_time2 = datetime.now(pytz.timezone(
                'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")  # second time

            different = float(currency_at_the_beginning) - \
                float(currency_after)
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
                data = f'{operation_number}\nWas {currency_at_the_beginning} {current_time1} Ok\nBecame {currency_after} {current_time2} {different}\n-----------------------------------------\n'
                file.write(data)

            # logging if OK
            logging.info(f'OK, operation  number:{operation_number}')

        except Exception as err:
            print(err)
            logging.exception(err, exc_info=True)  # logging if  NOT OK
            time.sleep(10)
            pass

        operation_number += 1


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window() as main_window:

    with dpg.group(horizontal=True):
        dpg.add_listbox(items=['RUB'], width=200, tag='currency_1')
        dpg.add_listbox(items=list_of_currencies, width=200, tag='currency_2')

    check_time = dpg.add_input_text(label='check time(sec)', tag='check_time')
    dpg.add_button(label='Start', callback=main)

    dpg.add_spacer(height=10)
    dpg.add_text('not set', tag='info')


dpg.set_viewport_title("currency monitoring")
dpg.set_primary_window(main_window, True)
dpg.set_viewport_width(450)
dpg.set_viewport_height(500)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
