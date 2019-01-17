#!usr/bin/env python
#encoding:utf-8
from __future__ import division


'''
__Author__:沂水寒城
功能：Pandas数据框索引函数 iloc、loc和ix学习使用
'''


'''
Pandas库中有iloc和loc以及ix可以用来索引数据，抽取数据。
loc函数是通过行标签索引行数据 
iloc函数是通过行号索引行数据 
ix函数是通过行标签或者行号索引行数据，简单来说就是loc和iloc的混合体 
iloc主要使用数字来索引数据，而不能使用字符型的标签来索引数据。而loc则刚好相反，只能使用字符型标签来索引数据，
不能使用数字来索引数据，不过有特殊情况，当数据框dataframe的行标签或者列标签为数字，loc就可以来其来索引。
ix是一种混合索引，字符型标签和整型数据索引都可以
'''
import sys
import pandas as pd
import numpy as np
reload(sys)
sys.setdefaultencoding('utf-8')


def testFunc():
    '''
    '''
    data=np.arange(36).reshape(6,6)
    print 'data:'
    print data
    df=pd.DataFrame(data)
    print 'dataFrame:'
    print df
    print '-*'*30
    print df.loc[1]
    print '-*'*30
    print df.iloc[1]
    print '-*'*30
    print df.loc[:,[0,4]]
    print '-*'*30
    print df.iloc[:,[0,4]]
    print '-*'*30

    print u"将数值型索引替换为字符型索引："
    df.index=['ID','Number','Height','Weight','Circle','Space'] 
    print df 
    print '-*'*30
    try:
        print df.loc[0]
    except Exception,e:
        print 'Exception: ',e
    print '-*'*30
    try:
        print df.iloc['Height'] 
    except Exception,e:
        print 'Exception: ',e
    print '-|=|'*30
    print df.iloc[0] 
    print df.loc['Circle']
    print '-*'*30
    
    print u"将数值型列索引替换为字符型列索引："
    df.columns=['zero','one','two','three','four','five']
    print df
    print '-*'*30
    print df.loc[:,'zero']
    print '-*'*30

    try:
        print df.iloc[:,'one'] 
    except Exception,e:
        print 'Exception: ',e
    print '-*'*30

    print u"ix抽取数据示例"
    print df.ix[5]
    print '-*'*30
    print df.ix[:,'three']
    print '-*'*30
    print df.ix[:,'one']
    print '-*'*30
    print df.ix[:,'five']

    print u"获取多行数据："
    print df.loc['Height':'Space']
    print df.iloc[2:]
    print df.ix['Height':'Space']
    print df.ix[2:]

    print '*%'*40

    print u"获取多列数据："
    print df.loc[:,'zero':'four']
    print df.iloc[:,0:5]
    print df.ix[:,'zero':'four']
    print df.ix[:,0:5]



if __name__=='__main__':
    testFunc()