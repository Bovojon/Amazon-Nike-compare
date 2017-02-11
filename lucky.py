#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Loading...')

search = raw_input("Please enter a search: ")

with open('data.html', 'wb') as f:
    response = requests.get('http://google.com/search?q=' + ' '.join(search), stream=True)
    response.raise_for_status()

    if not response.ok:
        print("There was an error")

    for block in response.iter_content(1024):
        f.write(block)

f.close()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(open("data.html"), "lxml")
print("Jelo")
# Open a browser tab for each result.
linkElems = soup.select('.r a')
print(linkElems)
numOpen = min(2, len(linkElems))
for i in range(numOpen):
    print("Working?")
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
