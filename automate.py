import webbrowser
import requests
import bs4


res = requests.get('https://automatetheboringstuff.com/chapter11/')
res.raise_for_status()
fileName = open(res.text)
# The bs4.BeautifulSoup() function returns is a BeautifulSoup object.
noStarchSoup = bs4.BeautifulSoup(fileName.read(), "lxml")
elems = noStarchSoup.select(".book")
print(type(elems))
print(len(elems))
print(type(elems[0]))
elems[0].getText()
str(elems[0])
elems[0].attrs

#print(type(noStarchSoup))


# playFile = open("romeojuliet.text", "wb")
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()
