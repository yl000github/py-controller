#! /usr/bin/env python
# -*- coding: utf-8 -*-
import win32api,win32gui,win32con
def findWindow(title,className=None):
    return win32gui.FindWindow(className,title);

def sendMessage(handle,message):
    handle.se
def getTitle(handle):
    return win32gui.GetWindowText(handle).decode('GB2312')
    
def getMessage(handle):
    buffer = '0' *50
    len = win32gui.SendMessage(handle, win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度
    win32gui.SendMessage(handle,win32con.WM_GETTEXT, len, buffer)
    return buffer
# 测试demo
handle=findWindow(None,'Notepad++')
print "窗体句柄",handle
print "窗体名",getTitle(handle)
# 查找编辑框
dlg = win32gui.FindWindowEx(handle, None, 'Edit', None)
print "窗体内容",getMessage(dlg)


