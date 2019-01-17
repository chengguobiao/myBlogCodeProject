#!usr/bin/env python
#encoding:utf-8


'''
__Author__:沂水寒城
功能：python基于给定时间戳生成 未来/过去  前进/倒退  n个小时的时间戳
'''


import datetime


def getBeforeTime(timestamp,hours,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 hours 个小时得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(hours):
        now_time-=datetime.timedelta(hours=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureTime(timestamp,hours,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 hours 个小时得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(hours):
        now_time+=datetime.timedelta(hours=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


if __name__=='__main__':
    timestamp='2018-12-19 11:00:00'
    getBeforeTime(timestamp,15,format='%Y-%m-%d %H:%M:%S')
    print '-*'*40
    getFutureTime(timestamp,15,format='%Y-%m-%d %H:%M:%S')