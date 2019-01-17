#!usr/bin/env python
#encoding:utf-8
from __future__ import division


'''
__Author__:沂水寒城
功能：python datetime 常用操作总结
'''

import time
import datetime


def generateNextTimestamp(start='2018-12-07 11:35:13',num=30):
    '''
    以给定的当前时刻为起点，生成未来时刻的时间戳（以小时为例）
    '''
    res_list=[]
    now_time=datetime.datetime.now()
    now_time=datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
    for i in range(num):
        now_time+=datetime.timedelta(hours=1)
        next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
        print next_timestamp
        res_list.append(next_timestamp)
    print res_list
    return res_list


def datetime2String(timestamp,format='%Y-%m-%d %H:%M:%S'):
    '''
    把datetime转成字符串
    '''
    res=timestamp.strftime(format)
    print 'res: ',res
    return res


def string2Datetime(timestamp,format='%Y-%m-%d %H:%M:%S'):
    '''
    把字符串转成datetime
    '''
    res=datetime.datetime.strptime(timestamp,format)
    print 'res: ',res
    return res


def string2Timestamp(timestamp):
    '''
    把字符串转成时间戳形式
    '''
    res=time.mktime(string2Datetime(timestamp).timetuple())
    print 'res: ',res
    return res


def timestamp2String(timestamp,format='%Y-%m-%d %H:%M:%S'):
    '''
    把时间戳转成字符串形式
    '''
    res=time.strftime("%Y-%m-%d-%H", time.localtime(timestamp))
    print 'res: ',res
    return res


def datetime2Timestamp(one_data):
    '''
    把datetime类型转为时间戳形式
    '''
    res=time.mktime(one_data.timetuple())
    print 'res: ',res
    return res


def string2Array(timestr='2018-11-11 11:11:11',format='%Y-%m-%d %H:%M:%S'):
    '''
    将字符串转化为时间数组对象
    '''
    timeArray=time.strptime(timestr,format)
    print 'timeArray: ',timeArray     
    print 'year: ',timeArray.tm_year
    print 'month: ',timeArray.tm_mon
    print 'day: ',timeArray.tm_mday
    print 'hour: ',timeArray.tm_hour
    print 'minute: ',timeArray.tm_min
    print 'second: ',timeArray.tm_sec


def getNowTime():
    '''
    获取当前时间
    '''
    now=datetime.datetime.now()
    print 'now: ',now
    timeStamp=now.strftime("%Y-%m-%d %H:%M:%S")
    print 'timeStamp: ',timeStamp 
    timeStamp2=now.strftime("%Y-%m-%d %H-%M-%S")
    print 'timeStamp: ',timeStamp2
    timeStamp3=now.strftime("%Y/%m/%d/%H/%M/%S")
    print 'timeStamp: ',timeStamp3 


def calTimeDelta(timestamp1='2018-11-16 19:21:22',timestamp2='2018-12-07 10:21:22',format='%Y-%m-%d %H:%M:%S'):
    '''
    计算给定的两个时间之间的差值
    '''
    T1=datetime.datetime.strptime(timestamp1,format)
    T2=datetime.datetime.strptime(timestamp2,format)
    delta=T2-T1
    day_num=delta.days
    sec_num=delta.seconds
    print 'day_num: ',day_num
    print 'sec_num: ',sec_num




if __name__=='__main__':
    generateNextTimestamp(start='2018-12-07 11:35:13',num=30)
    print '-*'*40
    datetime2Timestamp(datetime.datetime.now())
    print '-*'*40
    datetime2String(datetime.datetime.now(),format='%Y-%m-%d %H:%M:%S')
    print '-*'*40
    string2Datetime('2018-12-07 11:35:13',format='%Y-%m-%d %H:%M:%S')
    print '-*'*40
    string2Timestamp('2018-12-07 11:35:13')
    print '-*'*40
    timestamp2String(time.time(),format='%Y-%m-%d %H:%M:%S')
    print '-*'*40
    string2Array()
    print '-*'*40
    getNowTime()
    print '-*'*40
    calTimeDelta()