


#数据库
import pymysql

china_stock_conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='5279888',
    db='china_stock',
    port=3306,
    charset='utf8'
)
