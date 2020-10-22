import pymssql


class MSSQL:
    host = ""
    username = ""
    passwrd = ""
    dbname = ""
    encoding = "UTF-8"

    def __init__(self, host,username,passwrd,dbname):
        self.host = host
        self.username = username
        self.passwrd = passwrd
        self.dbname = dbname

        print("数据库连接初始化")

    def __GetConnnect(self):
        self.conn = pymssql.connect(self.host, self.username, self.passwrd, self.dbname, "UTF-8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "数据库连接获取失败！")
        else:
            return cur

    def ExecQuery(self, sql):
        cur = self.__GetConnnect()
        cur.execute(sql)
        result = cur.fetchall()

        self.conn.close()
        return result

    def ExecNoQuery(self, sql):
        cur = self.__GetConnnect()
        cur.execute(sql)
        self.conn.commiy()
        self.conn.close()

def main():
        m = MSSQL(host="127.0.0.1", username="robin", passwrd="test123123", dbname="pythontest")
        result_1 = m.ExecQuery("select id, number,convert(nvarchar(50),S_name) as S_name,S_age from students")
        print(result_1)


if __name__ == "__main__":
    main()