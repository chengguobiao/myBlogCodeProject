#!usr/bin/env python
#encoding:utf-8
from __future__ import division

'''
__Author__:沂水寒城
功能： python 基于滑动平均思想实现简易的缺失数据填充
'''




def zeroDataFill(one_all_list):
    '''
    对于0数据处理,简单实现版本,可忽略
    '''
    res_list=[]
    for i in range(len(one_all_list)):
        if one_all_list[i]!=0:
            res_list.append(one_all_list[i])
        else:
            if i==0:
                for j in range(1,len(one_all_list)):
                    if one_all_list[j]!=0:
                        res_list.append(one_all_list[j])
                        break
            elif i==len(one_all_list)-1:
                res_list.append(int(sum(res_list[-3:-1])/2))
            else:
                tmp=0
                for j in range(i,len(one_all_list)):
                    if one_all_list[j]!=0:
                        tmp=one_all_list[j]
                        break
                now=(res_list[i-1]+tmp)/2
                res_list.append(int(now))
    print res_list
    return res_list




def dataProcessing(one_all_list,num=7):
    '''
    对于时间序列数据中的 0 进行处理，采用滑动平均的方法来填充(默认时间为一周)
    '''
    nozero_list=[one for one in one_all_list if one!=0]
    before_avg,last_avg=sum(nozero_list[:num])/num,sum(nozero_list[-1*num:])/num
    res_list=[]
    for i in range(len(one_all_list)):
        if one_all_list[i]!=0:
            res_list.append(one_all_list[i])
        else:
            tmp=int(num/2)+1
            if i<=tmp:
                res_list.append(int(before_avg))
            elif i>=len(one_all_list)-tmp:
                res_list.append(int(last_avg))
                slice_list=one_all_list[i-tmp:i+tmp+1]
                res_list.append(int(sum(slice_list)/(num-1)))
    print res_list
    return res_list


if __name__=='__main__':
    one_all_list=[0,12,3,5,1,5,7,8,4,0,12,14,0,0,45,34,67,43,0,9,1,0]
    zeroDataFill(one_all_list)
    dataProcessing(one_all_list,num=7)