# -*- coding: UTF-8 -*-
import json
# from _ctypes import Array
# 几个要素
# 1.多线程
# 2.自定义爬取规则  ok
# 3.异常控制  ok
# 4.断点继续
# 5.重试
class Crawler:
    def __init__(self,urls,dir,headers,filename):
        self.curRs=urls
        self.dir=dir
        self.headers=headers
        self.filename=filename
        self.time=0
    
    def then(self,fn):
        if self.curRs is None:
            raise "self.cusRs为空，无法继续"
        self.time+=1
        arr=[]
        for obj in self.curRs:
            try:
                rs=fn(obj)
                if rs is not None:
                    if isinstance(rs, list):
                        for detail in rs:
                            arr.append(detail)
                    else:        
                        arr.append(rs)
            except Exception,e:
                print "解析出错，第",self.time,"轮",obj," 异常信息",str(e)
        self.curRs=arr
        print "第",self.time,"次的结果为",self.curRs
#         save current result
        self.saveRs()
        return self
    def saveRs(self):
        '''
            存储文件名规则，crawler文件名-轮数.txt
        '''   
        obj={
            "dir":self.dir,
            "headers":self.headers,
            "curRs":self.curRs,
            }
        content=json.dumps(obj)
#         content="\n".join(self.curRs)
        path="crawler-tmp/"+self.filename+"-"+str(self.time)+".txt"         
        fo = open(path, "w")
        fo.write(content)
        fo.close()
    def saveDB(self):
        '''
                            存储到数据库    
        '''
        
#         self.cusRs=urls
#         self.dir=dir
#         self.headers=headers
# def then(self,fn):