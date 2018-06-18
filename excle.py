#!/user/bin/env python
# coding:utf8
#python操作excel获取excle里面的数据  pip install xlrd
__author__ = 'liyatao'
import xlrd,random
def excle(exclename):
    #---------------获取excle中提前准备好的用户名与密码---------------------
    data=xlrd.open_workbook(exclename)  #用xlrd打开excle表格,其中exclename为excle的文件名加后缀
    # table=data.sheets()[0]  #通过索引顺序获取
    table=data.sheet_by_index(0)  #通过索引顺序获取
    # table=data.sheet_by_name(u'Sheet0') #通过名称获取
    nrows=int(table.nrows)         #获取表格行数
    #nclos=int(table.ncols)         #获取表格列数

    #----随机选择一个账号---
    list=[]
    for num in range(0,nrows):
        list.append(num)      #根据总共有多少个账号生成 一个列表
    x=random.sample(list,1)[0]    #生成一个随机数，那随即选取一个账号密码

    print nrows  #总共有多个行
    print x  #横座票
    username=table.cell(x,0).value.encode('utf8') #按座标（方块）获取数据 这里获取的是左边第x行第1列 用户名 座标（x,0）
    password=table.cell(x,1).value.encode('utf8') #按座标（方块）获取数据 这里获取的是左边第1行第2列的 密码

    print username,password

if __name__=="__main__":
    exclename="username.xls"
    excle(exclename)
