from background_task import background
import time

@background
def task_hello(schedule=1, repeat =2):
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Ym, %H:%M:%S",time_tuple)
    print("task .... Hello World!",time_str)

@background
def crawling_cpu(schedule=60,repeat =60*60*24):
    url= 'https://quasarzone.com/bbs/qn_hardware?_method=post&_token=K88Lvs0XlVzI1qWCg3O4BtDyDW4hmt8w3b33aw0V&category=CPU%\2FMB%\2FRAM&kind=subject&sort=num%2C%\20reply&direction=DESC&page=1'
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
                link = link.get('href')    
                cur.execute("INSERT INTO cpu_table (title,link) VALUES (?,?)",(title,link))
            con.commit()    
        print('task_crawling_quasar_zone_cpu : ',type(links),len(links))

    #add crawling
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Ym, %H:%M:%S",time_tuple)
    print("task_crawling_cpu",time_str)


@background
def crawling_gpu(schedule=60,repeat =60*60*24):

    url = 'https://quasarzone.com/bbs/qn_hardware?_method=post&_token=K88Lvs0XlVzI1qWCg3O4BtDyDW4hmt8w3b33aw0V&category=%\EA%B7%B8%\EB%\9E%\98%\ED%\94%BD%\EC%B9%B4%\EB%\93%9C&kind=subject&sort=num%2C%\20reply&direction=DESC&page=1'
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
                link = link.get('href')    
                cur.execute("INSERT INTO gpu_table (title,link) VALUES (?,?)",(title,link))
            con.commit()    
        print('task_crawling_quasar_zone_gpu : ',type(links),len(links))

    #add crawling
    time_tuple = time.localtime()
    time_str = time.strftime("%m/%d/%Ym, %H:%M:%S",time_tuple)
    print("task_crawling_gpu",time_str)


