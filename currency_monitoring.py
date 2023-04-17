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


def close_programm():
    print("INPUT ERROR")
    to_exit = input("PRESS ENTER FOR EXIT")
    exit()


try:
    from config import API_KEY 

except ImportError:
    print('API_KEY is now found or not set!')
    close_programm()

logging.basicConfig(
    level=logging.INFO,
    filename="log_currency.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")


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


def query_execution(operation_number):
    first_currency = dpg.get_value('currency_1')
    second_currency = dpg.get_value('currency_2')
    # СБОР НЫНЕШНЕГО КУРСА ВАЛЮТ
    URL = (
        f'https://currate.ru/api/?get=rates&pairs={first_currency}{second_currency}&key={API_KEY}')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
    full_page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    soup_text = soup.getText()
    soup_dict = ast.literal_eval(soup_text)
    if soup_dict['status'] == '500':
        print('Internal Server Error\nThis means that there may not be such a pair of currencies on the currency.ru server, it is recommended to choose other currencies!')
        return close_programm()
    data = soup_dict["data"][first_currency + second_currency]
    return data


def main():
    first_currency = dpg.get_value('currency_1')
    second_currency = dpg.get_value('currency_2')
    check_time = round(float(dpg.get_value('check_time')))

    if first_currency == second_currency:
        print('Two identical currencies!')
        return close_programm()
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

           
            logging.info(f'OK, operation  number:{operation_number}') # logging if OK

        except Exception as err:
            print(err)
            logging.exception(err, exc_info=True)# logging if  NOT OK
            time.sleep(10)  
            pass

        operation_number += 1


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window() as main_window:

    with dpg.group(horizontal=True):
        dpg.add_listbox(items=list_of_currencies, width=200, tag='currency_1')
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
