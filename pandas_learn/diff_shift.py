#!usr/bin/env python
#encoding:utf-8
from __future__ import division

'''
__Author__:沂水寒城
功能：Pandas diff和shift函数学习
'''



'''
diff函数是用来将数据进行某种移动之后与原数据进行比较得出差异数据
函数形式：
DataFrame.diff(periods=1, axis=0)
参数解释：
periods：移动的幅度
axis：移动的轴（按列移动或者按行移动）


shift函数是对数据进行移动的操作
函数形式：
DataFrame.shift(periods=1, freq=None, axis=0)
参数解释：
periods：移动的幅度
axis：移动的轴（按列移动或者按行移动）
shift(n):  n>0，表述数据框向下移动，索引不会移动，只有数据移动，若移动后数据缺失则填充为NaN
           n<0，表述数据框向上移动，索引不会移动，只有数据移动，若移动后数据缺失则填充为NaN
'''

import numpy as np 
import pandas as pd


def testFunc():
    '''
    diff和shift函数学习
    '''
    data=np.arange(36).reshape(12,3)
    print 'data:'
    print data
    df=pd.DataFrame(data)
    print 'df:'
    print df.head(5)
    print df.info()
    print '-*'*40
    print df.diff()
    print '-*'*40
    print df-df.shift()
    print '-*'*40
    print df-df.shift()==df.diff()
    
    print '-*'*40
    print df.shift(1)
    print '-*'*40
    print df.shift(-1)
    print '-*'*40
    print df.shift(1,axis=1)
    print '-*'*40
    print df.shift(-1,axis=1)
    


if __name__=='__main__':
    testFunc()