
from bs4 import c
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import pymysql 
import json
import re

"""
db = pymysql.connect(
    host = " ",
    user = " ",
    password = " ",
    database = " ",
    charset='utf8mb4',
)
"""
question = []
lists = []

headers = requests.utils.default_headers()
headers.update({'User-Agent':'Mozilla/5.0'})

# 지금 한 번 사이트 검색하는거니까 for문을 한 번 만 도는 것!
# SQL사용할 수 있으면 한 번 확인해볼것!

# var1 이 0 인이유?


base_url = "https://www.heykorean.com/web/us/"                  # 메인화면
url = "https://rent.heykorean.com/web/us/property/list?cp="     # 특정화면  (어떤 특정화면???)

driver = webdriver.Chrome('C:/Users/user/AppData/Local/Programs/Python/chromedriver.exe')
# driver.get("https://rent.heykorean.com/web/us/property/list?cp=1") 

content = driver.page_source
soup = BeautifulSoup(content,"lxml")

res = requests.get("https://rent.heykorean.com/web/us/property/list?cp=1")
soup = BeautifulSoup(res.content, 'html.parser')

title = soup.select_one('div#container   div#rent-list-container   div#title-text')

print(title.get_text())

"""
#fetching URLs 
rents = soup.find_all('a', attrs={'class':'title-text'})
print(str(rents))
"""

"""
import requests
from bs4 import BeautifulSoup

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('http://v.media.daum.net/v/20170615203441266')

# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, 'html.parser')

# 3) 필요한 데이터 검색
title = soup.find('title')

# 4) 필요한 데이터 추출
print(title.get_text())
"""

"""
    for rent in rents:
            x = rent.get("href")
            link = urljoin(base_url,x)
            lists.append({"url": link})
            # print(lists)
     
    cursor = db.cursor()

    for info in lists:

        samplePage = requests.get(info["url"], headers=headers)
        bs = BeautifulSoup(samplePage.text, 'html.parser')
        # print(link)
        users = bs.find_all('span', attrs = {'class':'d-none'})
        titles = bs.find_all('a', attrs = {'class':'question-hyperlink'})
        for title,user in zip (titles,users):
            title = titles[0].text
            user = users[0].text
            question.append({"title": title ,"User_id" : user})
            print(question)
        
        driver.quit()

"""
#         ###  INSERT RECORD  ### 
#             insert = "INSERT INTO mty.rent_sample(title, rent_type, rent_location, rent_price) VALUES ('{0}', '{1}', '{2}', '{3}')".format(title_list,rent_room,rent_loc,rent_price)
#             cursor.execute(insert)
#             remaining_rows = cursor.fetchall()  ## fetches all the rows of a query result
#             # db.commit()
#             print(cursor.rowcount, "Record Inserted")
#             db.rollback()
# db.close()


# ###  CREATE A TABLE  ###
# create = "CREATE TABLE mty.rent_sample(id INT NOT NULL AUTO_INCREMENT, title VARCHAR(100), rent_type VARCHAR(50),rent_location VARCHAR(50), rent_price VARCHAR(50), primary key (id))"
# cursor.execute(create) 
# print("Table has been create successfully ... ")
# # db.commit()
# db.close()


# ###  DISPLAY RECORD  ###   
# select = "SELECT * FROM mty.sample_hk"
# cursor.execute(select)
# remaining_rows = cursor.fetchall() 
# print("Total number of record: ", cursor.rowcount)  
# print("Rent Information")
# # print(remaining_rows)
# for i in remaining_rows:
#     id = i[0]
#     title = i[1]
#     rent_type = i[2]
#     rent_location = i[3]
#     rent_price = i[4]
#     print(id, title, rent_type, rent_location, rent_price)
# cursor.close()
# db.close()
# print("MySQL connection is closed")    


# # ###  UPDATE RECORD  ###
# update = "UPDATE mty.sample_hk SET id = 40 WHERE id = 39 " 
# cursor.execute(update)
# # db.commit()
# print("Record updated successfully ...")
# db.rollback()
# db.close()
 



#       # from application1.py

#         #  tables = bs.find_all('table')[0].find_all('tr')
#         #  for table in tables:
#         #     # info1 = table.find_all('td')[0].text
#         #     info = table.find_all('td')[1].text.strip()
#         #     inform = []
#         #     # inform = inform.replace('/n', '')
#         #     # inform = inform.replace('/t','')
#         #     inform.append(info)
#         #     print(inform)
            

#         # hosts = bs.find_all('div', attrs = {'class':'content'})
#         # #i = hosts[1]
#         # # print(hosts[1].text)
#         # for host in hosts:
        
#         #     # host_info = []
#         #     # host_info.append(i.text.strip())
#         #     # print(host_info)
           
#         #     host_id = host.select('span')[1].text.strip()
#         #     host_email = host.select('span')[2].text.strip()
#         #     host_phone = host.select('span')[4].text.strip()
#         #     host_info=[]
#         #     host_info.append(host_id)
#         #     host_info.append(host_email)
#         #     host_info.append(host_phone)
#         #     print(host_info)