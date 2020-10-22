import pymssql


class MSSQL:
    host=""
    username=""
    passwrd=""
    dbname=""
    encoding="UTF-8"

    def __init__(self, host,username,passwrd,dbname,encoding):
        self.host=host
        self.username=username
        self.passwrd=passwrd
        self.dbname=dbname
        self.encoding=encoding