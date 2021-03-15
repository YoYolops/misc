import requests

url = 'https://ws.sandbox.pagseguro.uol.com.br/v2/checkout?email=yohanhxh@gmail.com&token=353512CEA97840C28FCCDEB21C60FF55'

headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
}

payload = {
    "email": "yohanhxh@gmail.com",
    "token": "353512CEA97840C28FCCDEB21C60FF55",
    "currency": "BRL",
    "itemId1": "0001",
    "itemDescription1": "Serviço Lopes Advocacia",
    "itemAmount1": "500.00",
    "itemQuantity1": "1",
    "itemWeight1": 5
}

response = requests.post(url, data=payload, headers=headers)

print(type(payload))
print(response)