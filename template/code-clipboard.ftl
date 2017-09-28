##java代码
% for column in columnList:
	obj.put("${column}", jsonObject.get("${column}"));
% endfor

##接口测试json报文
{
% for i,kv in enumerate(kvList):
	% if i!=len(kvList)-1:
	"${kv["key"]}":"${kv["value"]}",
	% else:
	"${kv["key"]}":"${kv["value"]}"
	% endif
% endfor  
}

##序列
% for num in sequence:
Z201708010000${num}
% endfor