#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib.common import  log
from lib.file import  fileRead,fileWrite
import random

# def log(title,msg=""):
	# print("====={}====={}".format(title,msg))
	# return

# def fileWrite(path,content):
	# fo = open("path", "w")
	# fo.write( content);
	# fo.close()
	
# def fileRead(path):
	# fo = open("path", "r")
	# str=fo.read();
	# fo.close()
	# return str
print("hello")
if 1>=0 :
	print("true")
else :
	print("false")

if 1<=0 :
	print("true")
elif 33==22 :
	print("false")
else :
	print("no")
list=[1,2,3,4]
for i in list:
	print("current value:"+str(i))
for i in range(len(list)):
	print("current value:"+str(list[i]))
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
	print i,j

urls = ['http://mmjpg.com/mm/{cnt}'.format(cnt=cnt) for cnt in range(0, 7)]
print "urls.length",len(urls)
print "urls:",urls
# for url in urls:
	# print url
	
count=1
while count<9:
	print "count:",count
	count=count+1
else:
	print "count false:",count
	
	
list= range(1,10)
print "list:",list

list=[1,2,'3']
print "list:",list

print "list[1]:",list[1]

print "list[-1]:",list[-1]

del list[1]
print "after delete list:",list

fileWrite("f:/foo.txt","fuck you")

print "str in file:",fileRead("f:/foo.txt")

def func_a(func, *args, **kwargs):
    print(func(*args, **kwargs))

def func_b(*args):
    return args
func_a(func_b, 1, 2, 3)

def func_c(**args):
    return args
   
print func_c(hh="123",kk="xx") 

print '\r\n'.join(['http://thzbbt.net/thread-213795-2-1.html', 'http://thzbbt.net/thread-1255969-1-1.html'])

# print fileRead("crawler-tmp/crawler-thz-1.txt")

arr=[]
for i in xrange(26):
	arr.append(chr(i+ord('A')))
print arr
# print chr(random.randint(65, 90))
def a():
	return "22"
print "123"+"123"+a()+"123"+"123"+"1"

print "123"[-1]
print [1,2,3][-1]

import json 
print json.dumps([1,2,3,4])

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print text['a']


obj={
	'dd':'121'
	}
# if obj['dd1'] is None:
# 	print 'is'
# else:
# 	print 'no'
print obj.get('dd1','123')


arr=[1]
arr.append(None)
print arr
