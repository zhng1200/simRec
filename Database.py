#coding=utf-8
import pymysql
# 数据库操作类
class Database:
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "123", "neodb", charset="utf8")
        
        self.cursor = self.db.cursor()
    
    def query(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        results = self.cursor.fetchall()
        return results
        
    def execute(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        return 1
    
    def __del__(self):
        self.db.close()