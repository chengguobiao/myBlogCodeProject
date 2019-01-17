#!usr/bin/env python
#encoding:utf-8
from __future__ import division

'''
__Author__:沂水寒城
功能：  嵌套列表排序
'''

import operator


def sortFunc1(data_list,index=-3):
    '''
    借助于 operator 模块实现排序
    '''
    data_list.sort(key=operator.itemgetter(index)) 
    print '======================= sorted data_list ==================='
    print data_list


def sortFunc2(data_list,index=-3):
    '''
    基于内置函数 sorted  实现排序
    '''
    data_list=sorted(data_list,key=lambda i:i[index])
    print '======================= sorted data_list ==================='
    print data_list
    data_list.sort(key=lambda i:i[index], reverse=True)
    print '======================= sorted data_list ==================='
    print data_list


def sortFunc3(data_list):
    '''
    依据列表中元素的数量来排序
    '''
    data_list=sorted(data_list,key=lambda i:len(i))
    print '======================= sorted data_list ==================='
    print data_list


def sortFunc4(data_list):
    '''
    依据列表中元素总和来排序
    '''
    data_list=sorted(data_list,key=lambda i:sum(i))
    print '======================= sorted data_list ==================='
    print data_list


def sortFunc5(data_list):
    '''
    依据列表中元素绝对值的总和来排序
    '''
    data_list=sorted(data_list,key=lambda i:sum([abs(one) for one in i]))
    print '======================= sorted data_list ==================='
    print data_list


def sortFunc6(data_list):
    '''
    依据列表中元素最大值来排序
    '''
    data_list=sorted(data_list,key=lambda i:max(i))
    print '======================= sorted data_list ==================='
    print data_list


def sortFunc7(data_list):
    '''
    依据列表中元素最小值来排序
    '''
    data_list=sorted(data_list,key=lambda i:min(i))
    print '======================= sorted data_list ==================='
    print data_list


if __name__=='__main__':
    data_list=[['A',2,3,'apple','p',45,9],['D',23,13,'orange','q',23,19],['C',12,3,'banana','s',22,29],['E',42,23,'water','p',14,98],
               ['F',2,3,'snow','k',5,8],['G',12,43,'rain','m',41,12],['L',12,33,'ice','n',15,19],['O',12,13,'cream','b',31,25]]

    sortFunc1(data_list,index=-3)
    sortFunc2(data_list,index=-3)


    data_list=[['E',42,12,23,'p',14,98],['A','p',45,9],['D',13,'orange','q',23,19],['C',3,'s',22,29],['E',42,12,23,'water','p',14,98]]
    sortFunc3(data_list)


    data_list=[[42,12,23,14,98],[45,9],[13,-100,3,19],[6,3,-5,22,29],[42,12,23,14,98]]
    sortFunc4(data_list)
    sortFunc5(data_list)
    sortFunc6(data_list)
    sortFunc7(data_list)
