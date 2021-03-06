#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Run some automations to test things"""
from __future__ import unicode_literals
from __future__ import print_function

from pywinauto import application
#from pywinauto import tests
#from pywinauto.findbestmatch import MatchError


#application.set_timing(3, .5, 10, .5, .4, .2, .2, .1, .2, .5)

app = application.Application()
app.start(r"notepad.exe")

app['Notepad'].wait('ready')

app['Notepad'].menu_select("文件->页面设置")

# ----- Page Setup Dialog ----
# Select the 4th combobox item
app['页面设置']['ComboBox1'].select(4)

# Select the 'Letter' combobox item
app['页面设置']['ComboBox1'].select("Letter")

# ----- Next Page Setup Dialog ----
app['页面设置']['Printer'].click()

app['页面设置']['Network'].click()

# ----- Connect To Printer Dialog ----
# Select a checkbox
app['ConnectToPrinter']['ExpandByDef'].check()
# Uncheck it again - but use click this time!
app['ConnectToPrinter']['ExpandByDef'].click()

app['ConnectToPrinter']['OK'].close_click()

# ----- 2nd Page Setup Dialog again ----
app['PageSetupDlg2']['Properties'].click()

# ----- Document Properties Dialog ----
doc_props = app.window(title_re = ".*Document Properties")

# Two ways of selecting tabs
doc_props['TabCtrl'].select(2)
doc_props['TabCtrl'].select("Layout")

# click a Radio button
doc_props['RotatedLandscape'].click()
doc_props['Portrait'].click()

# open the Advanced options dialog in two steps
advbutton = doc_props['Advanced']
advbutton.click()

# ----- Advanced Options Dialog ----
# close the 4 windows
app.window(title_re = ".* Advanced Options")['Ok'].click()

# ----- Document Properties Dialog again ----
doc_props['Cancel'].close_click()
# ----- 2nd Page Setup Dialog again ----
app['PageSetup2']['OK'].close_click()
# ----- Page Setup Dialog ----
app['PageSetup']['Ok'].close_click()

# type some text
app['Notepad']['Edit'].set_edit_text("I am typing s\xe4me text to Notepad"
    "\r\n\r\nAnd then I am going to quit")

# exit notepad
app['NotepadDialog'].menu_select("File->Exit")
app['Notepad']['No'].close_click()

