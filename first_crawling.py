import requests
from bs4 import BeautifulSoup
import sqlite3

# CPU / MB / RAM
# CREATE cpu/mb/ram page table
# Crawling 43 page 2020.01~

conn=sqlite3.connect('db.sqlite3')
query='CREATE TABLE cpu_table (title TEXT,link TEXT)'
conn.execute(query)
conn.commit()
conn.close()
url = 'https://quasarzone.com/bbs/qn_hardware?_method=post&_token=K88Lvs0XlVzI1qWCg3O4BtDyDW4hmt8w3b33aw0V&category=CPU%2FMB%2FRAM&kind=subject&sort=num%2C%20reply&direction=DESC&page='
for page in range(1,43+1):
  res = requests.get(url+str(page))
  if res.status_code ==200:
    soup = BeautifulSoup(res.content,'html.parser')
    links =soup.find_all('a',class_='subject-link')
    with sqlite3.connect("db.sqlite3") as con:
        cur = con.cursor()
        title = ''
        link = ''
        for link in links:
            title = str.strip(link.get_text())
            link = link.get('href')
            #print(title+"                             "+link) 
            cur.execute("INSERT INTO cpu_table (title,link) VALUES (?,?)",(title,link))
        con.commit()
    #print('page No: '+str(page))
print('task_crawling_quasar_zone : ',type(links),len(links)) 


# GPU
# CREATE cpu/mb/ram page table
# Crawling 23 page

conn=sqlite3.connect('db.sqlite3')
query='CREATE TABLE gpu_table (title TEXT,link TEXT)'
conn.execute(query)
conn.commit()
conn.close()

url = 'https://quasarzone.com/bbs/qn_hardware?_method=post&_token=K88Lvs0XlVzI1qWCg3O4BtDyDW4hmt8w3b33aw0V&category=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&kind=subject&sort=num%2C%20reply&direction=DESC&page='

for page in range(1,23+1):
  res = requests.get(url+str(page))
  if res.status_code ==200:
    soup = BeautifulSoup(res.content,'html.parser')
    links =soup.find_all('a',class_='subject-link')
    with sqlite3.connect("db.sqlite3") as con:
        cur = con.cursor()
        title = ''
        link = ''
        for link in links:
            title = str.strip(link.get_text())
            link = link.get('href')
            #print(title+"                             "+link) 
            cur.execute("INSERT INTO gpu_table (title,link) VALUES (?,?)",(title,link))
        con.commit()
    #print('page No: '+str(page))
print('task_crawling_quasar_zone : ',type(links),len(links)) 

