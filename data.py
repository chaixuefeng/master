import pymysql

host = 'localhost'
user = 'root'
password = 'qinglong5'
database = 'firm'


# 增加用户
def insert(param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    sql = 'insert into zhengxuefengshigou  values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()


# 增删改
def updata(sql, param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    con.commit()
    cursor.close()
    con.close()


# 查
def select():
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    sql = 'SELECT * FROM zhengxuefengshigou'
    cursor.execute(sql)

    return cursor.fetchall()

    con.commit()
    cursor.close()
    con.close()

