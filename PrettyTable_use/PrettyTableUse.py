#!usr/bin/env python
#encoding:utf-8


'''
__Author__:沂水寒城
功能：  PrettyTable 模块使用   
'''

import sqlite3
import prettytable
from prettytable import from_csv
#from prettytable import from_cursor
from prettytable import PrettyTable



def testFunc1():
    '''
    '''
    table=PrettyTable()
    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_row(["Adelaide",1295, 1158259, 600.5])
    table.add_row(["Brisbane",5905, 1857594, 1146.4])
    table.add_row(["Darwin", 112, 120900, 1714.7])
    table.add_row(["Hobart", 1357, 205556, 619.5])
    table.add_row(["Sydney", 2058, 4336374, 1214.8])
    table.add_row(["Melbourne", 1566, 3806092, 646.9])
    table.add_row(["Perth", 5386, 1554769, 869.4])
    print '=================================table===================================='
    print table

    table.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
    table.add_column("Area",[1295, 5905, 112, 1357, 2058, 1566, 5386])
    table.add_column("Population",[1158259, 1857594, 120900, 205556, 4336374, 3806092,1554769])
    table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,869.4])
    print '=================================table===================================='
    print table


def testFunc2(data='mycsv.csv'):
    '''
    从 csv 文件中加载数据
    '''
    mycsv=open(data)
    table=from_csv(mycsv)
    mycsv.close()
    print '===========================================table=============================================='
    print table
    print '=================================table:SepalLength_Species===================================='
    print table.get_string(fields=['SepalLength','Species'])
    print '=======================================table:60=>80 rows======================================'
    print table.get_string(start=60,end=80)


def testFunc3(data='mycsv.csv'):
    '''
    从 数据库 中加载数据
    '''
    connection=sqlite3.connect("myDB.db")
    cursor=connection.cursor()
    cursor.execute("SELECT id,age,name FROM myTable")
    mytable=from_cursor(cursor)
    print '=================================table===================================='
    print table



if __name__=='__main__':
    testFunc1()

    testFunc2(data='iris.csv')