# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import crawler_sql
from bs4 import BeautifulSoup
from selenium import webdriver


def crawlerRuten(key):
    url = 'http://find.ruten.com.tw/search/s000.php?enc=u&searchfrom=searchf&k='
    searchUrl = url +key 
    driver = webdriver.PhantomJS(executable_path='C:\Program Files (x86)/phantomjs-2.1.1-windows/bin/phantomjs')
    driver.get(searchUrl)
    pageSource = driver.page_source
    Soup = BeautifulSoup(pageSource, 'lxml')
    driver.quit()
    
    P_IDS = Soup.find_all('a', attrs={'class':'link-favorite'})
    nameS = Soup.find_all('span', attrs={'class':'item-name-text'})
    priceS = Soup.find_all('strong', attrs={'class':'rt-text-price'})

    return nameS,priceS,P_IDS
 
NAME,PRICE,P_ID = crawlerRuten('cardistry')
sql = crawler_sql.Sql_Access('127.0.0.1','returnCardistry','ktk','ktkruten')
for i in range(len(NAME)):
    print(P_ID[i]['data-no'])
    print(NAME[i].text)
    print(len(NAME[i].text))
    print(PRICE[i].text)
    sql.insert(P_ID[i]['data-no'],NAME[i].text,PRICE[i].text)
