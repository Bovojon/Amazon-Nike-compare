import webbrowser
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))

# If there is an error in downloading the file, raise an error:
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" %(exc))

print(len(res.text))
print(res.text[:250])

webbrowser.open('http://inventwithpython.com/')
