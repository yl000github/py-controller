#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
class DB:
    def __init__(self,host,user,password,dbname,port=3306):
        self.host=host
        self.user=user
        self.password=password
        self.dbname=dbname
        self.port=port
        try:
            self.con=MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, port=self.port, db=self.dbname)
            self.cur=self.con.cursor()
            print "数据库初始化成功"
        except:
            raise "数据库无法连接"

    def close(self):
        """关闭数据库连接

        """
#         print "self.con",self.con
        if  self.con is not None:
            self.con.close()
        else:
            raise "数据库无法关闭"

    def query(self,sql):
        '''数据查询
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()

# db=MySQLdb.connect('192.168.1.15','ymt','yimiaotong2015','dlb')
# cursor=db.cursor()
# cursor.execute("select * from users")
# data=cursor.fetchone()
# print "data",data
# db.close()