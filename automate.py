import webbrowser
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

playFile = open("romeojuliet.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
