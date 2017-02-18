#! python3
# parse_html.py

import requests, sys, webbrowser, bs4
import json
import os
from flask import Flask, send_file, make_response, request, render_template, url_for, json

def parse_data():

    soupAmazon = bs4.BeautifulSoup(open("amazon.html"), "lxml")
    rows = soupAmazon.select('div.s-item-container')

    # Initialize lists
    matched_rows = []
    prices = []
    ratings = []
    descs = []

    for i in range(len(rows)):
        temp_string = str(rows[i])
        if "sx-price-whole" in temp_string:
            matched_rows.append(rows[i])

    for card in matched_rows:
        price = card.find_all("span", "sx-price-whole")
        rating = card.find_all("a", "a-popover-trigger")
        desc_h2 = card.find_all("h2",{"data-attribute":True})
        for des in desc_h2:
            desc = des["data-attribute"]

        prices.append(str(price))
        ratings.append(str(rating))
        descs.append(str(desc))

    char1 = '>'
    char2 = '</span>,'
    char3 = ', <span class="sx-price-whole">'
    char4 = '</span>]'
    lower = ''
    higher = ''
    rate = ''
    amazon_price_string = []
    amazon_rating_string = []

    for i in prices:
       if len(i) > 60:
        lower = i.partition(char1)[-1].rpartition(char2)[0]
        higher = i.partition(char3)[-1].rpartition(char4)[0]
        amazon_price_string.append(str("$"+lower+"-"+"$"+higher))
       else:
        individual = i.partition(">")[-1].rpartition("<")[0]
        amazon_price_string.append(str("$"+individual))


    for j in ratings:
        rate = j.partition('<span class="a-icon-alt">')[-1].rpartition('</span></i><i class="a-icon a-icon-popover">')[0]
        amazon_rating_string.append(rate)

    for i in range(len(amazon_rating_string)):
        if amazon_rating_string[i] == '':
            amazon_rating_string[i] = "No ratings."

    #for p in amazon_price_string:
    #    print p

    #for r in amazon_rating_string:
    #    print r

    #for d in descs:
    #    print d

    # fmt = '{:<100}{:<30}{}'
    # print(fmt.format('Name', 'Price', 'Rating'))
    # for i, (names, prices, ratings) in enumerate(zip(descs, amazon_price_string, amazon_rating_string)):
        # print(fmt.format(names, prices, ratings))



    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

    # print("Currrrrrrrrrrrrrrrrrent:")
    # print(SITE_ROOT)

    json_url = os.path.join(SITE_ROOT, "static/js", "amazon-output.json")

    # print("Currrrrrrrrrrrrrrrrrent:")
    # print(json_url)

    with open(json_url, "w") as outfile:
        json.dump({'names': descs, 'prices': amazon_price_string, 'ratings': amazon_rating_string}, outfile, indent=4)
