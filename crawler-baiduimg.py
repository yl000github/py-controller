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

import json
# lock = threading.Lock()     # 全局资源锁
# 提取数据、多线程、存储、异常处理、日志
initDir="f:/baiduimg-py/"
headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Referer":"https://image.baidu.com",
}
def first(word='蓝天',page='30',size='30'):
    url = "https://image.baidu.com/search/acjson"
    
    querystring = {"tn":"resultjson_com","ipn":"rj","ct":"201326592","is":"","fp":"result","queryWord ":"","cl":"2","lm":"-1","ie":"utf-8","oe":"utf-8","adpicid":"","st":"-1","word":word,"z":"","ic":"0","s":"","se":"","tab":"","width":"","height":"","face":"0","istype":"2","qc":"","nc":"1","fr":"","step_word":word,"pn":page,"rn":size,"gsm":"21c","1508403601126":""}
    
    headers = {
        'accept': "text/plain, */*; q=0.01",
        'x-devtools-emulate-network-conditions-client-id': "06ad5445-2692-4efa-861d-d62208efc17e",
        'x-requested-with': "XMLHttpRequest",
        'x-devtools-request-id': "4812.5709",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        'referer': "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%93%9D%E5%A4%A9&oq=%E8%93%9D%E5%A4%A9&rsp=-1",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cookie': "closedowntip=1; BDIMGISLOGIN=0; winWH=%5E6_2133x1067; BDqhfp=%E8%93%9D%E5%A4%A9%26%260-10-1undefined%26%2612358%26%2621; __cfduid=d4b3e0d936e446ae1150e319e977e1a571500017655; BAIDUID=F17E2CB6AC948CF68ABE48E54227229D:FG=1; PSTM=1500709607; BIDUPSID=21673F7FFA1CBA815D4EED0EF7E14524; Hm_lvt_b0e17e90eff522755fac9e19f71a97f7=1502439582,1502439582,1502439714; tip_show_limit=2; Hm_lvt_9a586c8b1ad06e7e39bc0e9338305573=1502439744,1502971293; MCITY=-%3A; BDUSS=1RrU3oxT2N0QUFmcmFMUFU0RVp3Q1Q1VTdncEx3bXYwUn5HUlVTcHdvNGdWZzVhSUFBQUFBJCQAAAAAAAAAAAEAAAA38WwXeWwwMDBiZAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDJ5lkgyeZZU; BDSFRCVID=ZJIsJeC62w2bEerZTIeiMiDG7gK2e-JTH6aooRlaLqXmzw6GEV7CEG0Pfx8g0KubHvB8ogKK3gOTH4nP; H_BDCLCKID_SF=tR32Wn7a5TrDHJTg5DTjhPrMbpoibMT-027OKKOa0qRooxbGDMO1XRkB0n_qeRTWWa6k-bv-thF0hCtCj5Abej5MKxobaRj-K5PXQbTEKJD_fbjv-4Qoq4tehH4tJR3eWDTm_Do4-nQ1DbrL3Mra3futQ-tfahOTtec9-pPKKR7IOM7yBP7R5RJb3aDLQJcB3mkjbPjDfn02OP5Py4ccQP4syP4eKMRnWnnXbIFKtDI2hCt6ePOq5-_th2TJ24oQaPo2WbCQMDTmqpcNLTDK0RI9DpbaXq3A3PjuBlbTJ-JFO-OxXpO1j4_e2f7f2pKLtIrZo4IE-Mch_p5jDh3a25ksD-Rtex7t227y0hvctb3cShPmhl00D6OXDNDtt5ts-DTbB4oHK--_qnTz-4L_5-_e-xQyetJyaR3J2RvbWJ5TMCo-Kh3njbDl3-r-0xr03gkf-prmJn_bShPC-tnlMt4VjNtj2toL5G7xKboO3l02V-jIe-t2ynLVbRjA24RMW20e0h7mWIb_VKFlej0Me53XDNRHK430-DT2LTrb2R6DHjrm-tnD-tRH-UnLqhTZW67Z0l8Ktt0KHl5NKl6xytLtXfrR05bMWbr-slcmWIQHDn7-h-QdKqkD2ltq0MQpJ274KKJx5tPWeIJo5t515xjbhUJiB5JMBan7_nrxfJOKHICGDj-WjMK; PSINO=6; H_PS_PSSID=1456_21081_17001_24022_22158; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E8%93%9D%E5%A4%A9%22%2C%22%E7%82%B9%E7%87%83%E7%9A%84%E9%85%92%E7%B2%BE%22%2C%22%E9%85%92%E7%B2%BE%22%2C%22%E9%85%92%E5%90%A7%22%2C%2297%E9%A6%99%E6%B8%AF%E5%9B%9E%E5%BD%92%22%2C%22%E9%A6%99%E6%B8%AF%E5%9B%9E%E5%BD%92%22%2C%22%E6%97%A7%E7%82%89%22%2C%22%E6%9E%97%E4%BF%8A%E6%9D%B0%22%2C%22%E9%85%92%E7%AA%9D%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; userFrom=www.baidu.com",
        'cache-control': "no-cache",
        'postman-token': "c76410c0-09d0-ba8b-daf1-b6750effb3b0"
        }
    
    jsonstr = requests.request("GET", url, headers=headers, params=querystring).text
#     print jsonstr
    obj=json.loads(jsonstr)
    data=obj['data']
    print 'data.length',len(data)
    arr=[]
    for item in data:
#         print item['middleURL']
        if item.has_key('middleURL'):
            arr.append(item['middleURL'])
#     print(response.text)
    return arr

initUrls=first(word='美女')
print "initUrls",initUrls
def getCurFileName():
    filename=os.path.basename(__file__)
    return filename[0:filename.find(".")]

crawler=Crawler(initUrls,initDir,headers,getCurFileName());
print "crawler初始化成功"
def fn1(url):
    return url
# def fn2(url):
#     r = requests.get(url, headers=headers, timeout=100).text
#     return BeautifulSoup(r, 'lxml').find('div',class_="content").find('a').img['src']
crawler.then(fn1)
# .then(fn2)








