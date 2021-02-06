import requests
from bs4 import BeautifulSoup

#Este módulo é responsável por pegar um html e retirar tabelas <table /> dele

def tableColector(url):
    link = url
    headers = {
        'Host': 'pre.ufcg.edu.br:8443',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://pre.ufcg.edu.br:8443/RelatoriosPRE/flow.html?_flowId=viewReportFlow&reportUnit=/Relatorios/Abertos/dadosUfcgPorPeriodo&j_username=anonymousUser&j_password=',
        'Connection': 'keep-alive',
        'Cookie': 'userLocale=pt_BR; JSESSIONID=E29883409FAF1521AC620AEFD15A1723; _ga=GA1.3.311544628.1598544732; 640508852e7be772c4b1f48198ebd0b9=566377b8f3od6bc9p5lr7rsv08',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

    html_bruto = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

    print(html_bruto.prettify())


tableColector('https://pre.ufcg.edu.br:8443/RelatoriosPRE/flow.html?_flowId=searchFlow&mode=library')

