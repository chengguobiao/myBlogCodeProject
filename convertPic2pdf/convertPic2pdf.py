#!usr/bin/env python
#encoding:utf-8
from __future__ import division


'''
__Author__:沂水寒城
功能： 将图片文件转化为PDF文件
'''

import os
import urllib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape,portrait



def downloadPics(img_url,file_path='filename'):
    '''
    从网络中下载图片
    python3 写法: urllib.request.urlretrieve(img_url,filename=file_path)
    '''
    urllib.urlretrieve(img_url,filename=file_path)


def convert_img_to_pdf(picDir,pdf_path):
    '''
    将图片转化为pdf
    '''
    pages=0
    (w,h)=landscape(portrait(A4))
    can=canvas.Canvas(pdf_path,pagesize=landscape(portrait(A4)))
    #获取img_path下文件，并进行排序
    files=os.listdir(picDir)
    files.sort(key=lambda x: len(x))  #依据图片名称长度升序排序
    # 遍历每个文件
    for f_name in files:
        # 拼装成完整的file路径
        file_path=picDir+os.sep+str(f_name)
        can.drawImage(file_path,0,0,w,h)
        can.showPage()
        pages=pages+1
    can.save()


if __name__=='__main__':
    convert_img_to_pdf('pics/','mypdf.pdf')