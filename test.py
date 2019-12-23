# sql 연결/해제

import pymysql

conn = pymysql.connect(
        host = " ", user = " ", password = " ", database = " ", charset='utf8mb4'
)

try:
    cur = conn.cursor()
    cur.execute(
        '''
        명령어
        '''
    )

finally:
    cur.close()
    conn.close()