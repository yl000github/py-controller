#!/usr/bin/env python
# coding=utf-8

import os
import time
import random
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup

from lib.common import log
from lib.file import fileRead
from lib.crawler import Crawler
import json
lock = threading.Lock()     # 全局资源锁
def uniqueKey():
    l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    timestamp=str(int(round(time.time()*1000)))
    return str(timestamp+''.join(random.sample(l,16)))

def savePic(url,dir,headers):
    print "开始下载",url
    try:
#         l=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#         timestamp=str(int(round(time.time()*1000)))
#         key=str(timestamp+''.join(random.sample(l,16)))
        imgpath=dir+uniqueKey()+".jpg"
        img=requests.get(url,headers=headers,timeout=100)
        if img.status_code==200:
            with open(imgpath,'ab') as f:
                f.write(img.content)
            print "下载完成",url
        else:
            raise "状态码不是200"
        return "success"
    except Exception as e:
        print e
        return "fail"
    

# print uniqueKey()
if __name__ == "__main__":
    print "开始"
#     TODO
    filepath="crawler-tmp/crawler-baiduimg-1.txt"
#     filepath="crawler-tmp/crawler-jandan-1.txt"
#     filepath="crawler-tmp/crawler-mmjpg-2.txt"

#     读取配置
    c=fileRead(filepath)
    obj=json.loads(c)
    print "obj",obj
    list=obj["curRs"]
    headers=obj["headers"]
    dir=obj["dir"]
    
    if not os.path.exists(dir) :
        os.mkdir(dir)
#     list=c.split("\n")
#     pool = Pool(processes=cpu_count())
    pool = Pool(4)
    result=[]
    for url in list:
        result.append(pool.apply_async(savePic, (url,dir,headers)))
    pool.close()
    pool.join()
    print "执行结果"
    for rs in result:
        print rs.get()
#     savePic(list[0])


