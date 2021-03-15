import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

#link: https://pre.ufcg.edu.br:8443/RelatoriosPRE/flow.html?_flowId=searchFlow&mode=library
#Este módulo é responsável por pegar um html e retirar tabelas <table /> dele


#def trial():

#    """ Dado uma URL e headers, a função retorna o HTML da página """

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

