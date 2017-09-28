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
initDir="f:/mmjpg-py/"
headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Referer":"http://www.mmjpg.com",
}
initUrls=["http://www.mmjpg.com/mm/{num}".format(num=num) for num in range(1,2)]
print "initUrls",initUrls
def getCurFileName():
    filename=os.path.basename(__file__)
    return filename[0:filename.find(".")]

crawler=Crawler(initUrls,initDir,headers,getCurFileName());
print "crawler初始化成功"
def fn1(url):
    r = requests.get(url, headers=headers, timeout=100).text
    maxCount=BeautifulSoup(r, 'lxml').find('div',class_="page").find_all('a')[-2].text
#     print maxCount
    page_urls = [url + "/" + str(i) for i in range(1, int(maxCount) + 1)]
    return page_urls
def fn2(url):
    r = requests.get(url, headers=headers, timeout=100).text
    return BeautifulSoup(r, 'lxml').find('div',class_="content").find('a').img['src']
crawler.then(fn1).then(fn2)








