'''
# sql 연결/해제

import pymysql

conn = pymysql.connect(
        host = " ", user = " ", password = " ", database = " ", charset='utf8mb4'
)

try:
    cur = conn.cursor()
    cur.execute(
       # 명령어
    )

finally:
    cur.close()
    conn.close()
'''
import time
from selenium import webdriver
 
# browser = webdriver.Firefox()
browser = webdriver.Chrome('C:/Users/user/AppData/Local/Programs/Python/chromedriver.exe')
browser.get("https://rent.heykorean.com/web/us/property/list?cp=1") 

inputElement = browser.find_element_by_class_name("title-text")
print(in)
'''
from selenium import webdriver
import time
 
browser = webdriver.Firefox()
browser.get("http://python.org")
 
menus = browser.find_elements_by_css_selector('#top ul.menu li')
 
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)
 
pypi.click()  # 클릭
 
time.sleep(5) # 5초 대기
browser.quit() # 브라우저 종료
'''
