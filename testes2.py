import requests

url = "http://cotacao.b3.com.br/mds/api/v1/DerivativeQuotation/DOL"
resp = requests.get(url)

""" bs = BeautifulSoup(resp.content) """

""" trs = bs.body.div.div.div.form.div.div.table.tbody.tr.find('td', id='TB03').content """

print(resp.content)

""" for tr in trs:
    if trs.index(tr) == 2:
        tds = tr.findAll("td")

        for td in tds:
            if tds.index(td) == 3:
                valor = td.get_text()

print(valor) """