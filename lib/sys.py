#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys  
import os.path  
import win32clipboard as w    
import win32con  
import win32api  
def getClipboardText():#读取剪切板  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_TEXT)  
    w.CloseClipboard()  
    return d  
def setClipboardText(aString):#写入剪切板  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_TEXT, aString)  
    w.CloseClipboard()  