#工具
#1 获取今日日期 格式 YYYY-MM-DD
import  datetime
import time

import  tushare as ts
import  pandas as pd

from  pytdx.util.best_ip import select_best_ip

# best_stock_ip = select_best_ip('stock')
# best_future_ip = select_best_ip('future')
best_stock_ip = {'ip': '123.125.108.23', 'port': 7709}
best_future_ip = {'ip': '124.74.236.94', 'port': 7721}
def get_today_date():
    return str( datetime.date.today())
def get_n_days_ago_date(n):
    d = datetime.date.today() - datetime.timedelta(n)
    return  str(d)
get_n_days_ago_date(2)
def get_all_cn_stock():
    pro = ts.pro_api('c70d79c6663a747b1c45416b02c0529b046a363c8d35faea73c6b19f')

    # 或者
    # pro = ts.pro_api('your token')

    df_SZSE = pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province,main_business,business_scope')
    df_SSE = pro.stock_company(exchange='SSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province,main_business,business_scope')
    df = df_SSE.append(df_SZSE, ignore_index=True)
    df.to_csv('/Users/zheng/Desktop/csv_data/stocks_furtures/all_cn_stocks.csv',encoding ="utf_8_sig")
    return  df

def get_all_cn_stocks__from_csv():
     df = pd.read_csv('/Users/zheng/Desktop/csv_data/stocks_furtures/all_cn_stocks.csv', encoding="utf_8_sig")
     all_stocks = df['ts_code']
     # print(all_stocks)
     return all_stocks.to_list()
# get_all_cn_stock()
# print(get_all_cn_stock_csv().head(10))
# print(type(get_all_cn_stock_csv()))
# print(get_all_cn_stock_csv().tail(1
# 0))

def show_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print ('程序 %s 的运行时间是:  %.2f' % (func.__name__ ,time.time() - local_time))
    return wrapper
#更改tushare 代码格式
def make_stock_code_for_BaoStock(stock_code):
    stock_code = ".".join(stock_code.lower().split('.')[::-1])
    return  stock_code

#清除日线重复数据
def cut_day_repeated_row(file_path,df):
     original_pd = pd.read_csv(file_path)
     for i,r in df.iterrows():
         if r['date'] in original_pd['date'].values :
             df.drop(i,inplace =True)
     return df


# 清除分钟重复数据
def cut_min_repeated_row(file_path, df):
    original_pd = pd.read_csv(file_path)
    for i, r in df.iterrows():
        if r['datetime'] in original_pd['datetime'].values:
            df.drop(i, inplace=True)
    return df
def make_datetime_str(time_str_):
    time_str = time_str_
    y, m, d, h, mi, s = time_str[0:4], time_str[4:6], time_str[6:8], time_str[8:10], time_str[10:12], time_str[12:14]
    datetime_str = y + '-' + m + '-' + d + ' ' + h + ":" + mi + ":" + s
    # print('====',time_str,"======",'++++++',datetime_str,'++++++')
    return datetime_str
def cut_datetime_str(s):
    s1 = s
    s2 = s1[:-6]
    return s2

