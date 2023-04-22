# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:27:26 2023

@author: novia
"""
import requests
from bs4 import BeautifulSoup
import sys

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

def query():
    try:
        kyword = sys.argv[1] 
        search_url = "https://tw.dictionary.search.yahoo.com/search?p="+kyword+"&fr2=sb-top&fr=sfp"
        res = requests.get(search_url,headers=headers)
        soup = BeautifulSoup(res.text,'lxml')
        # 判斷單字是否存在
        if soup.find("div",class_="w-100p"):
            err = soup.find("div",class_="w-100p")
            print(err.text)
        else:
            for dics in soup.find("div",class_="grp-tab-content-explanation"):
                if dics.find("span", class_="pos_button"):
                    att = dics.find("span", class_="pos_button")
                    print(att.text)
                for emp in dics.find_all("li"):
                    print(emp.text)
                    print('\n')
    except IndexError as e:
        print('錯誤訊息:', e)
        print('請輸入單字')    

if __name__ == "__main__":
    query()