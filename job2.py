import random,string
import os
import time
import shutil
from os.path import join, getsize
# 随机文件名
def genRandomString(slen=10):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))
#复制内容
def TXTRead_Writeline(text): 
    #读取文件
    for i in range(100):
        ms = open("copy.txt","r",encoding='utf-8')  
         #逐行写入
        for line in ms.readlines():  
            with open(text,"a",encoding='utf-8') as mon:
                mon.write(line) 
#创建文件夹
def mkdir(path): 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False
 #工作
def job():
   #循环数量
   getdirsize('c:\\temp2')
   now = int(time.time())
   timeArray = time.localtime(now)
   otherStyleTime = time.strftime("%Y%m%d", timeArray)
   a ="c:\\temp2\\" + otherStyleTime + "\\"
   mkdir(a)
   for i in range(10):
       file_name = a + genRandomString()+ '.txt'
       f = open(file_name,'w',encoding='utf-8')
       print ('创建成功'+ file_name)
       TXTRead_Writeline(file_name)
   f.close()
   
def deltemp():
    shutil.rmtree('c:\\temp2',ignore_errors=True)
    print('删除文件temp')

def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    a= size/1024/1024
    if a>5000:
       deltemp()
