#coding=utf-8
import os
import time
import zipfile
import tarfile

#压缩文件或文件夹为zip
def zip_dir(srcPath,dstname):
    zipHandle=zipfile.ZipFile(dstname,'w',zipfile.ZIP_DEFLATED)
    if os.path.isfile(srcPath):
        zipHandle.write(srcPath)
    else :
        for dirpath,dirs,files in os.walk(srcPath):
            print "dirs",dirs
            for filename in files:
                zipHandle.write(os.path.join(dirpath,filename)) #必须拼接完整文件名，这样保持目录层级
                print filename.decode('gbk')+" zip succeeded"

    zipHandle.close
    
def zip_dirs(srcPaths,dstname):
    zipHandle=zipfile.ZipFile(dstname,'w',zipfile.ZIP_DEFLATED)
    for srcPath in srcPaths:
        if os.path.isfile(srcPath):
            zipHandle.write(srcPath)
            print srcPath.decode('gbk')+" zip succeeded"
        else :
            for dirpath,dirs,files in os.walk(srcPath):
                for filename in files:
                    zipHandle.write(os.path.join(dirpath,filename)) #必须拼接完整文件名，这样保持目录层级
                    print filename.decode('gbk')+" zip succeeded"

    zipHandle.close

#解压zip文件
def unzip_dir(srcname,dstPath):
    zipHandle=zipfile.ZipFile(srcname,"r")
    for filename in zipHandle.namelist():
        print filename
    zipHandle.extractall(dstPath) #解压到指定目录

    zipHandle.close()


#压缩文件夹尾tar.gz
def tar_dir(srcPath,dstname):
    tarHandle=tarfile.open(dstname,"w:gz")
    for dirpath,dirs,files in os.walk(srcPath):
        for filename in files:
            tarHandle.add(os.path.join(dirpath,filename))
            print filename+" tar succeeded"

    tarHandle.close()

#解压tar.gz文件到文件夹
def untar_dir(srcname,dstPath):
    tarHandle=tarfile.open(srcname,"r:gz")
    for filename in tarHandle.getnames():
        print filename
    tarHandle.extractall(dstPath)
    tarHandle.close()
    
APPDATA=os.getenv("APPDATA");
p86=os.getenv("ProgramFiles(x86)");
p=os.getenv("ProgramFiles");
dir="d:/environment/";
config={
        "notepad++":[
                     p86+"/Notepad++/plugins",
                     APPDATA+"/Notepad++",
                     "C:/Users/Administrator/Downloads/npp_7.4.2_Installer.exe"
            ],
        "tomcat7":[
                     "D:/Program Files/tomcat",
            ],        
        "jdk8":[
                     "C:/Program Files/Java",
                     ],        
        "eclipse":[
                     "D:/eclipse-jee-mars-2-win32-x86_64 (1)/eclipse",
                     "D:/workspace/.metadata",
                     "D:/workspace/.recommenders",
                     ],        
        "python":[
                     "c:/Python27",
                     "C:/Users/Administrator/Downloads/python-2.7.13.msi",
                     ],        
}
if __name__ == "__main__":
#     zip_dir("f:/autocode","d:/environment/autocode.zip") #可以用绝对或者相对路径的文件名或文件夹名
#     zip_dirs(['f:/autocode','f:/bd-images','f:/0.png'], "d:/environment/autocode3.zip")
	list=[]
#     list.append('notepad++')
#     list.append('tomcat7')
    # list.append('jdk8')
# 	list.append('eclipse')
	list.append('python')
	for key in list:
		folders=config[key]
		zip_dirs(folders, dir+key+" "+time.strftime("%Y-%m-%d", time.localtime())+".zip")
    
