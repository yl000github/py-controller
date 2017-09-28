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
initDir="f:/thz/"
headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Referer":"http://thzbbt.net",
}
initUrls=["http://thzbbt.net/forum-181-{num}.html".format(num=num) for num in range(1,10)]
print "initUrls",initUrls

crawler=Crawler(initUrls,initDir,headers,"crawler-thz");
def fn1(url):
    arr=[]
    r = requests.get(url, headers=headers, timeout=100).text
    for father in BeautifulSoup(r, 'lxml').find_all('th',class_="common"):
        link=father.find_all("a")[3]["href"]
        arr.append("http://thzbbt.net/"+link)
    return arr
def fn2(url):
    arr=[]
#     print "url",url
    r = requests.get(url, headers=headers, timeout=100).text
    for father in BeautifulSoup(r, 'lxml').find_all('img',class_="zoom"):
        link=father["file"]
        arr.append(link)
    return arr
crawler.then(fn1).then(fn2)









