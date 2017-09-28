变量
hello ${name}
条件
% if condition<=0 :
	print("true")
% else :
	print("no")
% endif

循环
% for i in list:
	print("current value:"+str(${i}))
% endfor