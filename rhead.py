import requests

# USe Asocks to make IP proxies
proxies = {"http": "", "https": ""}    

a = requests.get("https://api.ipify.org/?format=json", proxies=proxies)

print(a.json())