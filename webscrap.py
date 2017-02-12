#! python3
# webscrap.py - Searched Amazon and Nike and compares prices
import webbrowser, requests, bs4
from get_data import get_keywords, get_data
from parse_html import parse_data

def present_prices():
    get_data()
    parse_data()

if __name__ == '__main__':
    present_prices()
