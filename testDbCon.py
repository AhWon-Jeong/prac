import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='nydb', charset='utf8')


# db 연결 함수
def conDB(con):
    print("===========연결됨===========")
    return con.cursor()

# db 연결해제 함수
def closeDB(con):
    print("===========해제함===========")
    con.close()

# db에서 사용자 input searc
def SearchData(searchword):
    curs = conDB(conn)
    sql = "select P_Title from PRIDATA where P_Title like %s"
    like_val = f'%{searchword}%'
    curs.execute(sql, like_val)

    data = curs.fetchall()
    for i in range(len(data)):
        print(data[i])
    closeDB(conn)

def selectall():
    curs = conDB(conn)
    sql = "select * from PRIDATA"
    curs.execute(sql)

    data = curs.fetchall()
    for i in range(len(data)):
        print(data[i])
    closeDB(conn)

word = input()
SearchData(word)
selectall()