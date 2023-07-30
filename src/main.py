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


def get_current_time(func):
    def wrapper(base_currencies: str,
                second_currency: str) -> tuple[requests.models.Response, str]:
        got_currencies = func(base_currencies, second_currency)
        current_time = datetime.now(pytz.timezone(
            'Europe/Moscow')).strftime("%H:%M:%S %Y-%m-%d")
        return got_currencies, current_time
    return wrapper


def error_exit_and_log(err: str) -> None:
    dpg.set_value('error_message', err)
    logger.error(err)
    return console.print(f'[red]{err}')


def write_in_history(
        operation_number: int,
        currency1: float,
        time1: str,
        currency2: float,
        time2: str,
        different_between_currencies_values: float) -> None:
    with open('history_of_currencies.txt', 'a') as file:
        file.write(f'\n{operation_number}\n')
        file.write(tabulate.tabulate([["Was",
                                       currency1,
                                       time1,

                                       'OK'],
                                      ["Became",
                                     currency2,
                                     time2,
                                     different_between_currencies_values]],
                                     tablefmt="simple",
                                     disable_numparse=False))
        file.write(f'\n')
    logger.info(f'Data with operation number {operation_number} was wrote')


def time_is_valid(_time: str) -> bool:
    if _time.isdigit():
        if int(_time) > 0:
            return True
    return False


def check_data_are_valid_and_start_loop() -> None:
    '''
    First function to start main loop:
    this is the initial function that checks
    the validity of the data before running
    the loop: it takes the primary and secondary
    currency and time from the GUI using dearpygui's
    built-in get_value function
    '''

    base_currencies = dpg.get_value('currency_1')
    second_currency = dpg.get_value('currency_2')
    wait_time = dpg.get_value('time_to_check')

    if base_currencies != second_currency:
        if time_is_valid(wait_time):
            dpg.set_value(
                'info', f"Set as: 1 {base_currencies} = {second_currency}")
            main_loop(base_currencies, second_currency, int(wait_time))
        else:
            return error_exit_and_log('Not valid time')
    else:
        return error_exit_and_log('Two identical currencies')


@get_current_time
def request_to_api_to_get_page(
        base_currencies: str,
        second_currency: str) -> tuple[requests.models.Response, str]:
    '''
    This function send one a request to the server
    and return page or close with error
    '''

    site_url = 'https://api.freecurrencyapi.com/v1/latest'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; \
        Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"}
    try:
        page = requests.get(
            site_url,
            params={
                'apikey': API_KEY,
                'base_currency': base_currencies,
                'currencies': second_currency},
            headers=headers)
        return page
    except requests.exceptions as err:
        return error_exit_and_log(err)


def page_status_code_is_valid(page: requests.models.Response) -> bool:
    '''
    This function check check response valid:
    if Ok - return True, else return False and print error
    '''

    try:
        if page.status_code == 200:
            logger.info(f'{page.status_code} {page.reason}')
            return True

        if page.status_code == 401:
            logger.info(f'{page.status_code} {page.reason}')
            error_exit_and_log(
                'Not valid API_KEY\nPlease check API_KEY from config.py is exist ')
            return False

        else:
            logger.info(f'{page.status_code} {page.reason}')
            error_exit_and_log(
                f'Sorry, program get error with code status: {page.status_code} {page.reason}')
            return False
    except Exception as err:
        logger.info(f'{page.status_code} {page.reason}')
        return False


def response_parser(page: requests.models.Response) -> float:
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_text = soup.getText()
    text = ast.literal_eval(soup_text)
    data = dict(text)['data']
    try:
        return float(list(data.values())[0])
    except ValueError:
        return error_exit_and_log('Server response is not float')


def main_loop(
        base_currencies: str,
        second_currency: str,
        wait_time: int) -> str:
    logger.info('Start loop')
    operation_number = 0
    while True:
        operation_number += 1

        first_response = request_to_api_to_get_page(
            base_currencies, second_currency)  # first data

        if page_status_code_is_valid(first_response[0]):
            currency_at_the_beginning = response_parser(first_response[0])
            current_time1 = first_response[1]
        else:
            return error_exit_and_log('Program don`t got data')

        # waiting time - maybe currencies values ate changed
        time.sleep(wait_time)

        second_response = request_to_api_to_get_page(
            base_currencies, second_currency)  # second data

        if page_status_code_is_valid(second_response[0]):
            currency_after = response_parser(second_response[0])
            current_time2 = second_response[1]
        else:
            return error_exit_and_log('Program don`t got data')

        different_between_currencies_values = \
            currency_at_the_beginning - currency_after

        print('\n', operation_number)
        print(tabulate.tabulate([
            ["Was",
             currency_at_the_beginning,
             current_time1,
             'OK'],

            ["Became",
             currency_after,
             current_time2,
             different_between_currencies_values]],
            tablefmt="simple",
            disable_numparse=True))

        write_in_history(
            operation_number,
            currency_at_the_beginning,
            current_time1,
            currency_after,
            current_time2,
            different_between_currencies_values)

        logging.info(f'Successful, operation  number:{operation_number}')


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
    dpg.add_button(label='Start', callback=check_data_are_valid_and_start_loop)
    
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
    dpg.destroy_context()
except KeyboardInterrupt:
    logger.info('Program was closed')
    console.print('[green1]Goodbye ')
    sys.exit()
except Exception as e:
    logger.exception(e)
    console.print(f'[red]{e}')
