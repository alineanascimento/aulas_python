print("\n importando modulo terceiro")

import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação http para {url} retornou o status code {response.status_code}")

