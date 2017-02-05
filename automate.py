import webbrowser
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

# If there is an error in downloading the file, raise an error:
res.raise_for_status()

print(len(res.text))
print(res.text[:250])

webbrowser.open('http://inventwithpython.com/')
