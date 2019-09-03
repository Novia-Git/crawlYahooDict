import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
import sys

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
kyword = sys.argv[1] 
if len(sys.argv) < 3:
    kyword2 = ''
else:
    kyword2 = sys.argv[2]
res = requests.get("https://tw.voicetube.com/definition/"+kyword,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

books = pd.Series()
if len(soup.select("div[id='definition']")) >= 1:
    for book in soup.select("div[id='definition']"):
        defLen = book.text.find('例句')
        dicName = book.text[3:defLen]
        dicEmp = book.text[defLen:]
    if kyword2 == '':
        print("解釋：")
        print(dicName)
        print('=========================================')   
    emp = book.text
else:
    if kyword2 == '':
        print("查無資料，請確認是否輸入正確？")

re = emp.find('例句',0,len(emp))

newstring = emp[re:].split('.')
if not kyword2:
    print('例句：')
examlist = []
for cont in newstring:
    if '例句' in cont:
        cont = cont.replace('例句','')
    if '。' in cont:
        cline = cont.index('。')
        #有句點斷行
        if kyword2 == '':
            print(cont[0:cline+1])
        examlist.append(cont[0:cline+1])
        #判斷有空白不要印       
        if cont[cline+1:] != ' ':
            if kyword2 == '':
                print(cont[cline+1:]+'.')
            examlist.append(cont[cline+1:]+'.')
    else:
        if kyword2 == '':
            print(cont+'.')
        examlist.append(cont+'.')
        
examlist = '\n'.join(examlist)
mydict = {kyword:[{'meaning':dicName,'example':examlist}]}

def wt2file(meaning,example):
    with open('mydict.txt','r') as f:
        con = f.read()
    key = kyword+':'
    if key not in con:
        with open('mydict.txt','a') as fw:
            fw.write(kyword+':'+'\n')
            fw.write(meaning)
            fw.write('例句:'+'\n')
            fw.write(example)
            fw.write('\n'+'=END='+'\n')
    else:
        print('已經加入過!')

def rd2file(key):
    with open('mydict.txt','r') as f:
        con = f.read()
    key = kyword+':'
    if key in con:
        st = con.find(key)
        en = con.find('=END=',st)
        print(con[st:en])
    else:
        print('此單字不存在，可以新增！')

def del2file(key):
    with open('mydict.txt','r') as f:
        con = f.read()
    key = kyword+':'
    if key in con:
        st = con.find(key)
        en = con.find('=END=',st)
        newdata = con.replace(con[st:en+6],'')
        with open('mydict.txt','w') as fw:
            fw.write(newdata)
    else:
        print('此單字不存在，無法刪除！')

#檢查有無單字檔
try:
    f=open('mydict.txt')
    f.close()
except:
    f=open('mydict.txt','w')
    f.close()
	
if kyword2 == 'add':
    wt2file(mydict[kyword][0]['meaning'],mydict[kyword][0]['example'])
if kyword2 == 'mylist':
    rd2file(kyword)
if kyword2 == 'del':
    del2file(kyword)
