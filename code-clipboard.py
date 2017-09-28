#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lib.common import log
from lib.constant import *
from lib.sys import getClipboardText
from lib.file import fileWrite
# print getClipboardText()
from mako.template import Template
log("程序开始")
ftl='''
#java代码
% for column in columnList:
    obj.put("${column}", jsonObject.get("${column}"));
% endfor

#接口测试json报文
{
% for i,kv in enumerate(kvList):
    % if i!=len(kvList)-1:
    "${kv["key"]}":"${kv["value"]}",
    % else:
    "${kv["key"]}":"${kv["value"]}"
    % endif
% endfor  
}

#序列
% for num in sequence:
Z201708010000${num}
% endfor
'''
# 处理输入
input=getClipboardText()
list=input.split("\r\n")
# print "list",list
if len(list)==2:
    start=int(list[0])
    end=int(list[1])
    sequence=['{cnt}'.format(cnt=cnt) for cnt in range(start, end)]

mytemplate = Template(text=ftl,input_encoding='utf-8',output_encoding='utf-8',default_filters=['decode.utf8'])
# mytemplate = Template(filename='template/code-clipboard.ftl',input_encoding='utf-8',output_encoding='utf-8',default_filters=['decode.utf8'])
outputContent=mytemplate.render(sequence=sequence,columnList=columnList,kvList=kvList)
print outputContent
import os
desktopPath=os.getenv("USERPROFILE")+"\Desktop"
outputPath=desktopPath+"\py-controller.txt"
print "outputPath",outputPath
fileWrite(outputPath,outputContent)