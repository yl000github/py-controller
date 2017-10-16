#-*-coding:utf-8-*-
import win32gui,win32con
#下面的是窗口的标题名称，这样是一定错的，但在控制台就可以正常使用
#写在文件里要用U编码
a=u".gitignore"
dlg=win32gui.FindWindow(None,a)
print "dlg",dlg
win32gui.CloseWindow(dlg)
# //用控件的ID取得控件的句柄，模拟写入输入框文本并按下提交按键
# t1=win32gui.GetDlgItem(dlg,1012)
# t2=win32gui.GetDlgItem(dlg,1001)
# k1=win32gui.GetDlgItem(dlg,1605)
# win32gui.SendMessage(t1,win32con.WM_SETTEXT,None,'902723')
# win32gui.SendMessage(t2,win32con.WM_SETTEXT,None,'761209')
# win32gui.SendMessage(k1,win32con.BM_CLICK,None,None)