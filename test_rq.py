import requests

json = {"key": ';"b)?gAfO\9Ks]d*$i7NP,~ #X0h[53y&}(vItl|ECW.VuH§T_-!oeR+/64qz82wpmcZ%UY@G=DkBj1FL', "text": "Fick dich"}

r = requests.post('http://212.87.214.127:8367/encrypt', json=json)

print(r.text)