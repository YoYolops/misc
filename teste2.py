import requests
from xml.etree import ElementTree

url = 'https://ws.sandbox.pagseguro.uol.com.br/v2/checkout?email={{email}}&token={{token}}'

headers = {
	'Content-Type': 'application/x-www-form-urlencoded',
}

payload = {
  'email': '{{email}}',
  'token': '{{token}}',
  'currency': 'BRL',
  'itemId1': '0001',
  'itemDescription1': 'Notebook Prata',
  'itemAmount1': '100.00',
  'itemQuantity1': 1,
  'itemWeight1': 1000,
  'reference': 'REF1234',
  'senderName': 'Jose Comprador',
  'senderAreaCode': 11,
  'senderPhone': 56713293,
  'senderCPF': 38440987803,
  'senderBornDate': '12/03/1990',
  'senderEmail': 'email@sandbox.pagseguro.com.br',
  'shippingType': 1,
  'shippingAddressStreet': 'Av.Brig.Faria Lima',
  'shippingAddressNumber': 1384,
  'shippingAddressComplement': '2o andar',
  'shippingAddressDistrict': 'Jardim Paulistano',
  'shippingAddressPostalCode': '01452002',
  'shippingAddressCity': 'Sao Paulo',
  'shippingAddressState': 'SP',
  'shippingAddressCountry': 'BRA',
  'extraAmount': -0.01,
  'redirectURL': 'http://www.seusite.com.br',
  'notificationURL': 'https://yourserver.com/nas_ecommerce/277be731-3b7c-4dac-8c4e-  4c3f4a1fdc46/',
  'maxUses': 1,
  'maxAge': 3000,
  'shippingCost': '1.00'
}

response = requests.post(url, data=payload, headers=headers)
string_xml = response.content
#xml_tree = ElementTree.fromstring(string_xml)

print(string_xml)
