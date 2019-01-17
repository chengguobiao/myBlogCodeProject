#!usr/bin/env python
#encoding:utf-8
 
 
'''
__Author__:沂水寒城
功能：python基于给定时间戳生成 未来/过去  前进/倒退  n个时刻的时间戳
'''
 
 
import datetime
 

def getBeforeSecond(timestamp,seconds,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 seconds 秒得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(seconds):
        now_time-=datetime.timedelta(seconds=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp 


def getBeforeMinute(timestamp,minutes,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 minutes 分钟得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(minutes):
        now_time-=datetime.timedelta(minutes=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp
 

def getBeforeHour(timestamp,hours,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 hours 个小时得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(hours):
        now_time-=datetime.timedelta(hours=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp
 

def getBeforeDay(timestamp,days,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 days 天得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(days):
        now_time-=datetime.timedelta(days=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getBeforeWeek(timestamp,weeks,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 weeks 个星期后得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(weeks):
        now_time-=datetime.timedelta(weeks=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getBeforeMonth(timestamp,months,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 months 个月后得到对应的时间戳
    '''
    from calendar import monthrange
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    year,month,day=[int(one) for one in str(now_time).split(' ')[0].split('-')]
    for i in range(months):
        now_time-=datetime.timedelta(days=monthrange(year,month)[1])
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getBeforeYear(timestamp,years,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，后退 years 年后得到对应的时间戳
    '''
    from calendar import monthrange
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    year,month,day=[int(one) for one in str(now_time).split(' ')[0].split('-')]
    for j in range(years):
        for i in range(12):
            now_time-=datetime.timedelta(days=monthrange(year,month)[1])
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureSecond(timestamp,seconds,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 seconds 秒得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(seconds):
        now_time+=datetime.timedelta(seconds=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureMinute(timestamp,minutes,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 minutes 分钟得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(minutes):
        now_time+=datetime.timedelta(minutes=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp
 

def getFutureHour(timestamp,hours,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 hours 个小时得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(hours):
        now_time+=datetime.timedelta(hours=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureDay(timestamp,days,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 days 天得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(days):
        now_time+=datetime.timedelta(days=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureWeek(timestamp,weeks,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 weeks 个星期后得到对应的时间戳
    '''
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    for i in range(weeks):
        now_time+=datetime.timedelta(weeks=1)
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureMonth(timestamp,months,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 months 个月后得到对应的时间戳
    '''
    from calendar import monthrange
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    year,month,day=[int(one) for one in str(now_time).split(' ')[0].split('-')]
    for i in range(months):
        now_time+=datetime.timedelta(days=monthrange(year,month)[1])
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp


def getFutureYear(timestamp,years,format='%Y-%m-%d %H:%M:%S'):
    '''
    以给定时间戳为基准，前进 years 年后得到对应的时间戳
    '''
    from calendar import monthrange
    now_time=datetime.datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
    year,month,day=[int(one) for one in str(now_time).split(' ')[0].split('-')]
    for j in range(years):
        for i in range(12):
            now_time+=datetime.timedelta(days=monthrange(year,month)[1])
    next_timestamp=now_time.strftime('%Y-%m-%d %H:%M:%S')
    print 'next_timestamp: ',next_timestamp
    return next_timestamp



 
if __name__=='__main__':
    #-----------------------------------------------------------------------------------------------
    #                                     生成过去时刻的时间戳
    #-----------------------------------------------------------------------------------------------
    getBeforeSecond('2018-12-19 11:00:00',40,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getBeforeMinute('2018-12-19 11:00:00',10,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getBeforeHour('2018-12-19 11:00:00',8,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getBeforeDay('2018-12-19 11:00:00',5,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getBeforeWeek('2018-12-19 11:00:00',2,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getBeforeMonth('2018-12-19 11:00:00',3,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getBeforeYear('2018-12-19 11:00:00',10,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    #-----------------------------------------------------------------------------------------------
    #                                     生成未来时刻的时间戳
    #-----------------------------------------------------------------------------------------------
    getFutureSecond('2018-12-19 11:00:00',40,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getFutureMinute('2018-12-19 11:00:00',10,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getFutureHour('2018-12-19 11:00:00',8,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getFutureDay('2018-12-19 11:00:00',5,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getFutureWeek('2018-12-19 11:00:00',2,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getFutureMonth('2018-12-19 11:00:00',3,format='%Y-%m-%d %H:%M:%S')
    print '=='*50
    getFutureYear('2018-12-19 11:00:00',10,format='%Y-%m-%d %H:%M:%S')
    print '=='*50