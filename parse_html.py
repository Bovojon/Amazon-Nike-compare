#! python3
# parse_html.py

import requests, sys, webbrowser, bs4

def parse_data():

    # Amazon - Retrieve data from first 5 results
    soupAmazon = bs4.BeautifulSoup(open("amazon.html"), "lxml")
    priceElemsAmazon = soupAmazon.select('.sx-price span')
    numAmazon = min(10, len(priceElemsAmazon))
    print("\n")
    print("Amazon prices range in: ")
    print("\n")
    for i in range(numAmazon):
        print(priceElemsAmazon[i])

    # Nike - Retrieve data from first 5 results
    soupNike = bs4.BeautifulSoup(open("nike.html"), "lxml")
    priceElemsNike = soupNike.select('span.local.nsg-font-family--base')
    numNike = min(10, len(priceElemsNike))
    print("\n")
    print("Nike prices range in: ")
    print("\n")
    for j in range(numNike):
        print(priceElemsNike[j])
