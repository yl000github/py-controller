#coding=utf-8
'''
数据库结构和excel相互转换
'''
from lib.db import DB
from lib.excel import readExcel,writeExcel
# xlrd.Book.encoding = "utf8"
def db2excel(db,tablename):
    rs=db.query('desc '+tablename)
    data=[]
    for row in rs:
        mix=row[1]
        t=mix.partition('(')
        if t[1]=='':
            type=mix
            length=''
        else:
            type=t[0]
            length=t[2][:len(t[2])-1]
        row=(row[0],type,'',length,row[3])
        data.append(row)
#         print row
#     print data
    writeExcel('f:/'+tablename+'.xlsx',data)
        
def excel2db(path):
    list=readExcel(path)
#     第一列为字段名
    

sqlExecute=DB('192.168.1.15','ymt','yimiaotong2015','dlb') 
db2excel(sqlExecute, 'users')
sqlExecute.close()  

# print 'int(11)'.partition('(')
# print 'int11)'.partition('(')
# print len('12312')
    

