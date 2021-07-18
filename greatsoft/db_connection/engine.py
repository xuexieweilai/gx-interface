import pymysql

class Engine(object):
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.1.72', user='root', password='123456',
                               db='aio_v3test')
        self.mycursor = self.conn.cursor()

    def get_userId_by_userName(self, userName):
        sql = "select id from sys_user where user_name=(%s);"
        self.mycursor.execute(sql, (userName,))
        datas = self.mycursor.fetchall()
        self.mycursor.close()
        self.conn.close()
        return datas[0][0]

    def get_pwd_by_userName(self, userName):
        sql = "select password from sys_user where user_name=(%s)"
        self.mycursor.execute(sql, (userName,))
        datas = self.mycursor.fetchall()
        self.mycursor.close()
        self.conn.close()
        print(datas)




# if __name__ == "__main__":
    # engine = Engine().get_userId_by_userName("TestL3")
    # engine = Engine().get_pwd_by_userName("TestL3")