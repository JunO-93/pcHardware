from background_task import background
import requests
from bs4 import BeautifulSoup
import time
import sqlite3

@background
def task_hello(schedule=10 , repeat =60):
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S",time_tuple)
    print("tasks........ Hello World!",time_str)

#@background()
def crawling_cpu(schedule=2,repeat =60*3): #schedule = 이게 실무에서 뜨는 시간을 이야기 하는 것 /repeat = 몇번 타임으로 repeat 하는가
    #add Crawling and insert to DB previously Code
    url= 'https://quasarzone.com/bbs/qn_hardware?_method=post&type=&page=1&_token=K88Lvs0XlVzI1qWCg3O4BtDyDW4hmt8w3b33aw0V&category=CPU%2FMB%2FRAM&kind=subject&keyword=&sort=num%2C+reply&direction=DESC'
    res = requests.get(url)
    if res.status_code ==200:
        soup = BeautifulSoup(res.content,'html.parser')
        links =soup.find_all('a',class_='subject-link')
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            title = ''
            link = ''
            for link in links:
                title = str.strip(link.get_text())
                link = 'https://quasarzone.com/'+link.get('href')    
                cur.execute("INSERT INTO cpu_table (title,link) VALUES (?,?)",(title,link))
            con.commit()    
        print('task_crawling_quasar_zone_cpu : ',type(links),len(links))
    
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S",time_tuple)
    print("task_crawling_cpu",time_str)


#@background()
def crawling_gpu(schedule=10,repeat =60*3):

    url = 'https://quasarzone.com/bbs/qn_hardware?_method=post&type=&page=1&_token=K88Lvs0XlVzI1qWCg3O4BtDyDW4hmt8w3b33aw0V&category=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&kind=subject&keyword=&sort=num%2C+reply&direction=DESC'
    res = requests.get(url)
    if res.status_code ==200:
        soup = BeautifulSoup(res.content,'html.parser')
        links =soup.find_all('a',class_='subject-link')
        with sqlite3.connect("db.sqlite3") as con:
            cur = con.cursor()
            title = ''
            link = ''
            for link in links:
                title = str.strip(link.get_text())
                link = 'https://quasarzone.com/'+link.get('href')    
                cur.execute("INSERT INTO gpu_table (title,link) VALUES (?,?)",(title,link))
            con.commit()    
        print('task_crawling_quasar_zone_gpu : ',type(links),len(links))
  
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Y, %H:%M:%S",time_tuple)
    print("task_crawling_gpu",time_str)


