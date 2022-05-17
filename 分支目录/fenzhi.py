# -*- encoding: utf-8 -*-
'''
@file: fenzhi.py
@time: 2022/5/17 9:54
@desc:
'''
import pymysql

# 打开数据库连接
db = pymysql.connect(
    host='132.246.27.59',
    user='aep_dev',
    passwd='24HeEZpEO&',
    db='aep_cpemgr_prod',
    port=28901,
    charset='utf8',
    # 以字典形式展示所查询数据
    cursorclass=pymysql.cursors.DictCursor)

try:
    with db.cursor() as cursor:  # 使用cursor()方法获取操作游标
        #   查询语句
        sql = "select * from device"
        cursor.execute(sql)  # 执行sql语句
        results = cursor.fetchall()  # 获取查询的所有记录
        for result in results:
            for key, value in result.items():
                print(key, value)
except Exception as e:
    print(e)
finally:
    db.close()  # 关闭连接
