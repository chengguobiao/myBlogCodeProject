#!usr/bin/env python
#encoding:utf-8
from __future__ import division


'''
__Author__:沂水寒城
功能：获取列表中最大/最小的前n个数值的位置索引
'''

import copy
import heapq


def getListMaxNumIndex(num_list,topk=3):
    '''
    获取列表中最大的前n个数值的位置索引
    '''
    max_num_index=map(num_list.index, heapq.nlargest(topk,num_list))
    min_num_index=map(num_list.index, heapq.nsmallest(topk,num_list))
    print 'max_num_index:',max_num_index
    print 'min_num_index:',min_num_index


def getListMaxNumIndex2(num_list,topk=3):
    '''
    获取列表中最大的前n个数值的位置索引
    '''
    tmp_list=copy.deepcopy(num_list)
    tmp_list.sort()
    max_num_index=[num_list.index(one) for one in tmp_list[::-1][:topk]]
    min_num_index=[num_list.index(one) for one in tmp_list[:topk]]
    print 'max_num_index:',max_num_index
    print 'min_num_index:',min_num_index


def getListMaxNumIndex3(num_list,topk=3):
    '''
    获取列表中最大的前n个数值的位置索引
    '''
    num_dict={}
    for i in range(len(num_list)):
        num_dict[i]=num_list[i]
    res_list=sorted(num_dict.items(),key=lambda e:e[1])
    max_num_index=[one[0] for one in res_list[::-1][:topk]]
    min_num_index=[one[0] for one in res_list[:topk]]
    print 'max_num_index:',max_num_index
    print 'min_num_index:',min_num_index


def getListMaxNumIndex4(num_list,topk=3):
    '''
    获取列表中最大的前n个数值的位置索引
    '''
    tmp_list=copy.deepcopy(num_list)
    max_num=sum([abs(O) for O in num_list])
    min_num=-1*max_num
    max_num_index,min_num_index=[],[]
    for i in range(topk):
        one_max_index=num_list.index(max(num_list))
        max_num_index.append(one_max_index)
        num_list[one_max_index]=min_num
    for i in range(topk):
        one_min_index=tmp_list.index(min(tmp_list))
        min_num_index.append(one_min_index)
        tmp_list[one_min_index]=max_num
    print 'max_num_index:',max_num_index
    print 'min_num_index:',min_num_index



if __name__=='__main__':
    num_list=[13,4,-8,3,1,43,55,2,7,11,78]
    getListMaxNumIndex(num_list,topk=3)

    getListMaxNumIndex2(num_list,topk=3)

    getListMaxNumIndex3(num_list,topk=3)

    getListMaxNumIndex4(num_list,topk=3)