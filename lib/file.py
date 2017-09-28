def fileWrite(path,content):
    fo = open(path, "w")
    fo.write( content);
    fo.close()
    
def fileRead(path):
    fo = open(path, "r")
    str=fo.read();
    fo.close()
    return str

