#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

conn= MySQLdb.connect(
        host='azure2.1more.cn',
        port = 3306,
        user='cdb',
        passwd='abcd_123',
        db ='cdb',
        )
cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

#查询数据库
cur.execute("select * from student")
#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

#一次插入多条记录
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
#     ])


#获取数据
data = cur.fetchall()

#打印数据
for r in data:
    print r

#关闭连接
cur.close()
conn.commit()
conn.close()