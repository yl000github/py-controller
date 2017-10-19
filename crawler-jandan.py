#!/usr/bin/env python
# coding=utf-8

import os
import time
import threading
from multiprocessing import Pool, cpu_count

import requests
from bs4 import BeautifulSoup

from lib.common import log
from lib.crawler import Crawler

# lock = threading.Lock()     # 全局资源锁
# 提取数据、多线程、存储、异常处理、日志
initDir="f:/jandan-py/"
headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Referer":"http://jandan.net",
}
# 最大208
initUrls=["http://jandan.net/ooxx/page-{num}#comments".format(num=num) for num in range(207,208)]
print "initUrls",initUrls
def getCurFileName():
    filename=os.path.basename(__file__)
    return filename[0:filename.find(".")]

crawler=Crawler(initUrls,initDir,headers,getCurFileName());
print "crawler初始化成功"
def fn1(url):
    arr=[]
    r = requests.get(url, headers=headers, timeout=100).text
    for father in BeautifulSoup(r, 'lxml').find_all('div',class_="row"):
        link=father.find("div",class_="text").img['src']
        arr.append('http:'+link)
    return arr
# def fn2(url):
#     r = requests.get(url, headers=headers, timeout=100).text
#     return BeautifulSoup(r, 'lxml').find('div',class_="content").find('a').img['src']
crawler.then(fn1)
# .then(fn2)








