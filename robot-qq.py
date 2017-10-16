#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pyautogui
import pyperclip
import time

class QQ:
    def __init__(self,titlepath,inputpath):
        self.inputloc=self.getPos(inputpath)
        self.titleloc=self.getPos(titlepath)
        x=(self.titleloc[0]+self.inputloc[0])/2
        y=(self.titleloc[1]+self.inputloc[1])/2
        self.chatloc=(x,y)
        print "=====初始化成功====="
        
    def show(self):
        print 'chatloc',self.chatloc
        print 'inputloc',self.inputloc
        
    def getPos(self,path):
#         print 'path',path
        loc=pyautogui.locateOnScreen(path)
#         print 'loc',loc
        if loc is None:
            pyautogui.hotkey('alt','tab')
            pyautogui.hotkey('alt','tab')
            loc=pyautogui.locateOnScreen(path)
        
#         print 'loc',loc
        if loc is None:
            raise Exception("初始化失败,无法确定坐标位置："+path)
        return pyautogui.center(loc)
    
    def sendMessage(self,msg=''):
        time.sleep(1)
        pyautogui.click(self.inputloc[0], self.inputloc[1])
        pyautogui.typewrite(msg)
        pyautogui.hotkey('alt','s')
    
    def getChatContent(self):
        time.sleep(1)
        pyautogui.click(self.chatloc[0], self.chatloc[1])
        pyautogui.hotkey('ctrl','a')
        pyautogui.hotkey('ctrl','c')
        return pyperclip.paste()

qq=QQ('f:/qun-title.png','f:/qun-input.png')
qq.show()
qq.sendMessage('hello world !')
print "chat content",qq.getChatContent().split("\r\n")[-2]
while 1:
    c=qq.getChatContent()
    print '最新一行',c.split("\r\n")[-2]
#     do something
    qq.sendMessage('1s')
    time.sleep(3)
    
    
    
    
    
    
    
# titleLoc=pyautogui.locateOnScreen('f:/qun-title.png')
# inputLoc=pyautogui.locateOnScreen('f:/qun-input.png')
# 
# 
# def getChatContent():
#     location = pyautogui.locateOnScreen('f:/qun-title.png')
# #     x,y=location[0]+



# pyautogui.hotkey('alt','tab')
# pyautogui.hotkey('alt','tab')
# pyautogui.hotkey('alt','tab')
# pyautogui.hotkey('alt','tab')
# pyautogui.hotkey('alt','tab')
# pyautogui.hotkey('alt','tab')
# pyautogui.typewrite('helloworld')
# pyautogui.hotkey('alt','s')

# location = pyautogui.locateOnScreen('f:/qun-input.png')
# location = pyautogui.locateOnScreen('f:/qun-title.png')
# print location

# pyautogui.password(text='', title='', default='', mask='*')

#  PyAutoGUI中文输入需要用粘贴实现
#  Python 2版本的pyperclip提供中文复制
# def paste(foo):
#     pyperclip.copy(foo)
#     pyautogui.hotkey('ctrl', 'v')
# 
# foo = u'学而时习之'
# #  移动到文本框
# pyautogui.click(800,500)
# paste(foo)