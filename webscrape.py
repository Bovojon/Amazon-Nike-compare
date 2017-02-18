#! python3
# webscrap.py - Searched Amazon and Nike and compares prices
import webbrowser, requests, bs4
from getData import get_data
from parse import parse_data

def present_prices(keyword):
    get_data(keyword)
    parse_data()

# if __name__ == '__main__':
#     present_prices()
