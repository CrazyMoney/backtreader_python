from functools import reduce
import numpy as np
import pymysql

con = pymysql.connect("127.0.0.1",
                      'root',
                      '5279888',
                      'test'
                      )
c = con.cursor()
for i in range(1000000):

    sql = "insert into table_name (name ,age,address,phone) values ('zheng',18,'山东省济宁市邹城市钢弹接到那市场伽马刀豆腐脑环境',13534955)"
    c.execute(sql)
con.commit()
con.close()