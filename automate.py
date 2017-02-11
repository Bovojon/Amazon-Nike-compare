#! python3
# automate.py - Searched Amazon and Nike and compares prices
import webbrowser, requests, bs4


print('Loading...')

search = raw_input("Please enter a search: ")
search = search.lower()
search = search.split(" ")
search = search[0]+"+"+search[1]

with open('data.html', 'wb') as f:
    response = requests.get('https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + ' '+search, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    }, stream=True)
    response.raise_for_status()

    if not response.ok:
        print("There was an error")

    for block in response.iter_content(1024):
        f.write(block)


# Retrieve top search result links.
soup = bs4.BeautifulSoup(open("data.html"), "lxml")
# Open a browser tab for each result.
linkElems = soup.select('.r a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

f.close()
