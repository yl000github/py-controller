#-*- coding: utf-8 -*-  ##设置编码方式

import win32api,win32gui,win32con

label = 'new 3.txt' #此处假设主窗口名为tt

hld = win32gui.FindWindow(None, label)
print "hld",hld
if hld > 0:
    dlg = win32gui.FindWindowEx(hld, None, 'Edit', None)#获取hld下第一个为edit控件的句柄
#     dlg = win32api.FindWindowEx(hld, None, 'Edit', None)#获取hld下第一个为edit控件的句柄

    buffer = '0' *50

    len = win32gui.SendMessage(dlg, win32con.WM_GETTEXTLENGTH)+1 #获取edit控件文本长度

    win32gui.SendMessage(dlg, win32con.WM_GETTEXT, len, buffer) #读取文本

    print buffer[:len-1]

    #虚拟鼠标点击按钮(或者回车)

    btnhld = win32gui.FindWindowEx(hld, None,'Button', None)

    # win32gui.PostMessage(btnhld, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

    # win32gui.PostMessage(btnhld, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    win32gui.PostMessage(btnhld, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)

    win32gui.PostMessage(btnhld, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    #获取显示器屏幕大小

    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)

    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    print "width",width
    print "height",height