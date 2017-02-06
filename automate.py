import webbrowser
import requests
import bs4


res = requests.get('http://nostarch.com')
res.raise_for_status()
# The bs4.BeautifulSoup() function returns is a BeautifulSoup object.
noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")
print(type(noStarchSoup))


# playFile = open("romeojuliet.text", "wb")
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()
