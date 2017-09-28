#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lib.common import log
from lib.sys import getClipboardText
log("123","sds")
# print getClipboardText()
from mako.template import Template
# print(Template("hello ${data}!").render(data="world"))
mytemplate = Template(filename='template/demo.ftl',input_encoding='utf-8',output_encoding='utf-8',default_filters=['decode.utf8'])
# print mytemplate.render(data="world",name="yanglin",condition=-4)
print mytemplate.render(data="world",name="样了呢",condition=-4,list=[1,2,3,4])
# 
# from mako import exceptions
# try:
#     print mytemplate.render(data="world",name="yanglin",columnList=columnList,kvList=kvList)
# except:
#     print(exceptions.text_error_template().render())