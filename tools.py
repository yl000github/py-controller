#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
'''
效果一般，说白也是调用dos指令
'''
def killPort(port):
    print 1
    ret = os.popen("netstat -nao | findstr "+port)
    str_list = ret.read().strip()
    print str_list
    ret_list = str_list.split(' ')
    print ret_list
    process_pid = ret_list[-1]
    print 'process_pid',process_pid
    os.system("taskkill /pid "+str(process_pid)+" /F")
#     os.system("kill -9 "+process_pid)


killPort("18080")