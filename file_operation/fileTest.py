#!usr/bin/env python
#encoding:utf-8
from __future__ import division



'''
__Author__:沂水寒城
功能：  文件操作汇总
'''



import os
import time
import datetime



 

def TimeStampToTime(timestamp):
    '''
    把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12
    '''
    timeStruct=time.localtime(timestamp)
    return str(time.strftime('%Y-%m-%d %H:%M:%S',timeStruct))

 
def get_FileSize(filePath):
    '''
    获取文件的大小,结果保留两位小数，单位为MB
    '''
    filePath=unicode(filePath,'utf8')
    fsize=os.path.getsize(filePath)
    fsize=fsize/float(1024*1024)
    return round(fsize,2)


def get_FileAccessTime(filePath):
    '''
    获取文件的访问时间
    '''
    filePath=unicode(filePath,'utf8')
    t=os.path.getatime(filePath)
    return TimeStampToTime(t)


def get_FileCreateTime(filePath):
    '''
    获取文件的创建时间
    '''
    filePath=unicode(filePath,'utf8')
    t=os.path.getctime(filePath)
    return TimeStampToTime(t)


def get_FileModifyTime(filePath):
    '''
    获取文件的修改时间
    '''
    filePath=unicode(filePath,'utf8')
    t=os.path.getmtime(filePath)
    return TimeStampToTime(t)


if __name__=='__main__':
    print get_FileSize('fileTest.py')
    print get_FileAccessTime('fileTest.py')