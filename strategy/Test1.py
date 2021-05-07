# import baostock as bs
# import pandas as pd
#
#
# def download_data(date):
#     bs.login()
#
#     # 获取指定日期的指数、股票数据
#     stock_rs = bs.query_all_stock(date)
#     stock_df = stock_rs.get_data()
#     data_df = pd.DataFrame()
#     print(stock_df)
#     # for code in stock_df["code"]:
#     #     print("Downloading :" + code)
#     #     k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
#     #     data_df = data_df.append(k_rs.get_data())
#     # bs.logout()
#     # data_df.to_csv("D:\\demo_assignDayData.csv", encoding="gbk", index=False)
#     # print(data_df)
#
#
# if __name__ == '__main__':
#     # 获取指定日期全部股票的日K线数据
#     download_data("2019-02-25")
DB_CONFIG= {
"host": '127.0.0.1',
"user" :'root',
"passwd":'5279888' ,
"port":3306,
"db":'china_stock',
"charset":'utf8'


}
import pymysql

conn = pymysql.connect(**DB_CONFIG)
cusor = conn.cursor()

rees = cusor.execute(
     " SELECT date FROM {} WHERE code='{}' order by date  limit 1".format('china_stock_day', 'sh.000001')
)
print(cusor.fetchall())