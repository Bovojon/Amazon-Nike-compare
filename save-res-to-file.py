import requests, sys, webbrowser, bs4

with open('test.txt', 'wb') as handle:
    response = requests.get('https://automatetheboringstuff.com/chapter11/', stream=True)

    if not response.ok:
        print("error")

    for block in response.iter_content(1024):
        handle.write(block)
