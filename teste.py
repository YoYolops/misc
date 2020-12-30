import requests

url = 'https://esb.tjpb.jus.br/cp-backend/sistemas/3/processos?nomeParte=Claudenir%20Lopes%20da%20Silva%20Barbosa&tipoPessoa=F&offset=0&quantidade=10'

headers = {
    'host': 'esb.tjpb.jus.br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'connection': 'keep-alive',
}

resposta = requests.get(url, headers=headers)

for i in resposta.json():
    print(i)
