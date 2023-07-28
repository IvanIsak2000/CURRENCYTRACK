import time
import sys
import logging
from datetime import datetime
from currencies_names import list_of_currencies
from config import API_KEY

import tabulate
import pytz
import ast
import requests
from rich.console import Console
from bs4 import BeautifulSoup
import dearpygui.dearpygui as dpg

console = Console()

logging.basicConfig(
    level=logging.INFO,
    filename="main.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")

logger = logging.getLogger(__name__)

def exit(err: str) -> None:
    sys.exit(err)

def write_in_history(
        operation_number: int,
        currency1: float,
        time1: str,
        currency2: float,
        time2: str,
        different: float) -> None:
    with open('history_of_currencies.txt', 'a') as file:
        data = f'''
№{operation_number}:
Was {currency1} {time1} Ok
Became {currency2} {time2} {different}
-----------------------------------------
'''
        file.write(data)
    logger.info(f'Data with operation number {operation_number} was wrote')

def time_is_valid(_time: str) -> bool:
    return _time.isdigit()


def query_execution(first_currency: str, second_currency: str) -> float:
    '''
    This function sends a request to the server
    and parses data from it: currency value
    '''

    try:
        site_url = 'https://api.freecurrencyapi.com/v1/latest'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}

        page = requests.get(
            site_url,
            params={
                'apikey': API_KEY,
                'base_currency': first_currency,
                'currencies': second_currency},
            headers=headers)

    except requests.exceptions as err:
        logger.error(err)
        return console.print(f'[red]{err}')

    
    match page.status_code:
        case 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            soup_text = soup.getText()
            text = ast.literal_eval(soup_text)
            data = dict(text)['data']
            return list(data.values())[0]

        case 401:
            logger.error('Not valid API_KEY')
            return console.print('[red]Not valid API_KEY\nPlease check API_KEY from config.py is exist!')
        
        case _:
            logger.exception('Code status: ', page.status_code)
            return console.print('[red]Sorry, program get error with code status: ', page.status_code)


def main_loop() -> str:

    first_currency = dpg.get_value('currency_1')
    second_currency = dpg.get_value('currency_2')

    if first_currency == second_currency:
        logger.exception('Two identical currencies!')
        return console.print('[red]Two identical currencies!')

    _time = dpg.get_value('time_to_check')

    if time_is_valid(_time):
        time_to_check = int(_time)
    else:
        logger.exception('Not integer time')
        return console.print('Time need to integer digit, for example: 10')



    dpg.set_value('info', f"Set as: 1 {first_currency} = {second_currency}")
    logger.info('Start loop')
    operation_number = 0
    while True:
        try:
            currency_at_the_beginning = query_execution(first_currency, second_currency)  # first data
            if currency_at_the_beginning != float:
                exit('Error: program don`t get data')
            current_time1 = datetime.now(pytz.timezone(
                'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")  # first time

            time.sleep(time_to_check)  # waiting

            currency_after = query_execution(first_currency, second_currency)  # second data
            current_time2 = datetime.now(pytz.timezone(
                'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")  # second time

            different = float(currency_at_the_beginning) - \
                float(currency_after)
            print('\n', operation_number)
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
            write_in_history(operation_number,
                             currency_at_the_beginning,
                             current_time1,
                             currency_after,
                             current_time2,
                             different)
            logging.info(f'OK, operation  number:{operation_number}')

        except Exception as e:
            logging.exception(e, exc_info=True)
            print(e)
            time.sleep(10)

        operation_number += 1


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window() as main_window:

    with dpg.group(horizontal=True):
        dpg.add_listbox(items=list_of_currencies, width=200, tag='currency_1')
        dpg.add_listbox(items=list_of_currencies, width=200, tag='currency_2')

    dpg.add_text('\n')
    time_to_check = dpg.add_input_text(
        label='check time(sec)', tag='time_to_check')
    dpg.add_button(label='Start', callback=main_loop)

    dpg.add_spacer(height=10)
    dpg.add_text('', tag='info')

    dpg.add_spacer(height=10)
    dpg.add_text('', tag='error_message', color=[255, 0, 0])


dpg.set_viewport_title("CURRENCYTRACK",)
dpg.set_primary_window(main_window, True, )
dpg.set_viewport_width(450)
dpg.set_viewport_height(500)
dpg.show_viewport()

try:
    dpg.start_dearpygui()
except KeyboardInterrupt:
    console.print('[green]Goodbye!')
    logger.info('Program was closed')
    sys.exit()
except Exception as e:
    console.print(f'[red]{e}')
    logger.exception(e)

dpg.destroy_context()
