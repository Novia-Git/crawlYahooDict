import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import sys

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
kyword = sys.argv[1]
res = requests.get("https://tw.voicetube.com/definition/"+kyword,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

books = pd.Series()
if len(soup.select("div[id='definition']")) >= 1:
    for book in soup.select("div[id='definition']"):
        defLen = book.text.find('例句')
        dicName = book.text[3:defLen]
    print(dicName)
else:
    print("查無資料，請確認是否輸入正確？")