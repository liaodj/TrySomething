"""
    作者：djliaoa
    功能：读表格，查快递
    版本：V1.0
    日期：2017-10-10
"""

#import csv
import xlrd
import requests

def main():
    # filepath = '10-9.xls'
    # with open(filepath, mode='r') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(', '.join(row))
    # !/usr/bin/env python
    # -*- coding: utf-8 -*-
    # 读取excel数据
    # 小罗的需求，取第二行以下的数据，然后取每行前13列的数据

    data = xlrd.open_workbook('10-9.xls')  # 打开xls文件
    table = data.sheets()[0]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    name_list = []
    for i in range(nrows):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        #print(table.row_values(i)[2])  # 取表格中第三行
        name_list.append(table.row_values(i)[2])
    # print(name_list)
    print(','.join(name_list))

    p = {}
    p['text'] = '邓金龙'  # 比如: 227728570825
    r = requests.get('http://ytozn.dh.cx/dea2a', timeout=30,params=p)
    print(r.status_code)
    print(r.text)



if __name__ == '__main__':
    main()