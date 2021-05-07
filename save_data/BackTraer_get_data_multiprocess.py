
"""
Backtrader
yfinance
BaoStock
"""
import pprint
import time
import  numpy as np
import baostock as bs
import pandas as pd
import tushare as ts
import  yfinance as yf
import pandas_datareader.data as web
import  pytdx
import  requests
import  sys
import  queue
import  QUANTAXIS as  QA
#### 登陆系统 ####
from pytdx.exhq import TdxExHq_API
from pytdx.params import TDXParams
from utils import (

    get_today_date,
    show_run_time,
    cut_day_repeated_row,
    cut_min_repeated_row,
    best_future_ip,
    best_stock_ip,
    get_n_days_ago_date,

    make_datetime_str, cut_datetime_str)


from settings import (
    csv_file_path,
    china_stock_day_file_path,
    china_stock_min_file_path,
    UsStock_list,
    us_stock_day_file_path,
    us_stock_min_file_path,
    China_fu_list,
china_furture_day_file_path,
china_furture_min_file_path,
china_all_stock_list,
)


#雅虎接口  获取美股数据 **多线程版**
class GetDateFromYahoo():
    def __init__(self,us_stock_list):
        self.stock_list = us_stock_list
    def get_us_stock_day(self,file_path,update = False,period='5y',interval="1d"):
        stock_dir ={}
        for s in self.stock_list:
            stock_dir[s] = yf.Ticker(s)
        for key,values in stock_dir.items():
             if update:
                 period='5d'
                 interval = '1d'
             result = values.history(period=period,interval=interval,
                start=None, end=None, prepost=False, actions=True,
                auto_adjust=True, back_adjust=False)
             result.columns= result.columns.map(str.lower)
             result.drop(['dividends','stock splits'],inplace=True,axis=1)
             result['date'] = result.index
             result['date'] = result['date'].apply(
                 lambda x: x.strftime("%Y-%m-%d"))
             if update:
                 result = cut_day_repeated_row(file_path+key+'.csv',result)
                 result.to_csv(
                     us_stock_day_file_path +  key + '.csv',
                     index=False,
                     mode = 'a',
                     header = False,
                 )
             else:
                result.to_csv(us_stock_day_file_path +  key + '.csv',index=False)
             print('美股日线保存成功:',key)
        print('-------------------美股日线完成----------------------')
    def get_us_stock_min(self,file_path, update=False, start=None, end=None, interval="5m"):  #获取美股5min
        stock_dir = {}
        for s in self.stock_list:
            stock_dir[s] = yf.Ticker(s)
        for key, values in stock_dir.items():
            result = values.history(
                                    interval=interval,
                                    start=start,
                                    end=end, prepost=False, actions=True,
                                    auto_adjust=True, back_adjust=False)
            result['datetime'] = result.index
            result['datetime'] = result['datetime'].apply(
                lambda x: x.tz_convert('America/New_York').strftime("%Y-%m-%d %H:%M:%S"))
            result.columns = result.columns.map(str.lower)
            try:
                result.drop(['dividends', 'stock splits'], inplace=True,axis=1)
            except:
                pass

            if update:
                result = cut_min_repeated_row(file_path+key+'.csv',result)
                result.to_csv(
                file_path+key+'.csv',
                index = False,
                mode = 'a',
                header = False,)
            else:
                result.to_csv(us_stock_min_file_path + key + '.csv', index=False)
            print('美股分钟保存成功:', key)
        print('--------------------美股分钟成功--------------------------')



#新浪 国内期货
class GetDataFromSina():
    def __init__(self,furture_list,):
        self.future_list = furture_list
    def get_cn_furture_day(self,file_path,update=False):
        for future in self.future_list:

            url_str = (
                        'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=' +
                        future)
            r = requests.get(url_str)
            r_json = r.json()
            r_lists = list(r_json)
            if update:  #更新
                r_lists = r_lists[-1]
            result = pd.DataFrame(data=r_lists,columns=['date','open','high','low','close','vol'])

            result = result.rename(columns={'vol': 'volume'})
            if update:
                 result = cut_day_repeated_row(file_path+future+'.csv',result)
                 result.to_csv(china_furture_day_file_path + future + '.csv',
                          index=False,
                          mode='a',
                          header=False
                          )
            else:
                result.to_csv(china_furture_day_file_path + future + '.csv', index=False)

            print('期货日线保存成功:', future)
        print('-------------------期货日线完成------------------------')

    def get_cn_furture_min(self,file_path,update=False):
        for future in self.future_list:
            url_str = (
                    'http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine15m?symbol=' +
                    future)
            r = requests.get(url_str)
            r_json = r.json()
            r_lists = list(r_json)[::-1]
            if update:
                r_lists= r_lists[-30:-1]

            result = pd.DataFrame(data=r_lists, columns=['datetime', 'open', 'high', 'low', 'close', 'vol'])
            result = result.rename(columns={'vol': 'volume'})
            if update:
                result = cut_min_repeated_row(file_path+future+'.csv', result)
                result.to_csv(china_furture_min_file_path + future + '.csv',
                              index=False,
                              mode= 'a',
                              header = False
                              )
            else:
                result.to_csv(china_furture_min_file_path + future + '.csv', index=False)

            print('期货分钟保存成功:', future)
        print('--------------------期货15分钟完成----------------------')
#
# baostock   = GetDataFromBaoStock(3,today_date= today_date,stock_list= china_all_stock_list)
#     baostock.get_china_stock_day_data(frequency='d',start_date='2006-01-01',end_date= today_date,file_path=china_stock_day_file_path,update=False)# 获取国内股票日线数据
#     baostock.get_china_stock_min__data(frequency='15',start_date='2015-01-01',end_date= today_date,file_path=china_stock_min_file_path,update=False)# 获取国内股票15min数据
#
#
#     #美股
#     n_day_ago = get_n_days_ago_date(59)
#
#     yahoo_ = GetDateFromYahoo(UsStock_list)
#     yahoo_.get_us_stock_day(file_path=us_stock_day_file_path)
#     yahoo_.get_us_stock_min(file_path=us_stock_min_file_path,start=n_day_ago,end=today_date)
#
#     #期货
#     sina_= GetDataFromSina(China_fu_list)
#     sina_.get_cn_furture_day(file_path=china_furture_day_file_path)
#     sina_.get_cn_furture_min(file_path=china_furture_min_file_path)

def get_china_stock_day_data(stock_list,start_date,end_date,file_path,update= False,frequency ="d"):   #获取国内日线
    if isinstance(stock_list,str):
        stock_list = [stock_list]
    for stock in stock_list:
            stock_code_  = ".".join(stock.lower().split('.')[::-1])
            rs = bs.query_history_k_data_plus(stock_code_,
                "date,code,open,high,low,close,volume,amount,turn,tradestatus,pctChg,isST,peTTM,pbMRQ,psTTM,pcfNcfTTM",
                start_date=start_date, end_date= end_date,
                frequency=frequency, adjustflag="2")
            data_list = []
            while (rs.error_code == '0') & rs.next():
                data_list.append(rs.get_row_data())
            result = pd.DataFrame(data_list, columns=rs.fields)
            if update:
                # with open(file_path+stock_code_+'.csv','a') as f:
                    # f.write('\n')

                result = cut_day_repeated_row(file_path + stock_code_ + '.csv',result)

                result.to_csv(
                    file_path + stock_code_ + '.csv',
                    index=False,
                    mode='a',
                    header=False,

                )
            else:
                result.to_csv(file_path+stock_code_+'.csv', index=False)
            print(" 国内日线完成:",stock_code_)
            # print( '进度:  %4.2f'% ((self.stock_list.index(stock)+1)/len(self.stock_list)))
    print('------------------国内日线成功---------------------------')

def get_china_stock_min__data(  stock_list,start_date, end_date, file_path, update=False,frequency= 15 ):
    #获取国内股票15min
    if isinstance(stock_list,str):
        stock_list = [stock_list]
    for stock in stock_list:
        stock_code_ = ".".join(stock.lower().split('.')[::-1])
        rs = bs.query_history_k_data_plus(stock_code_,
                                          "time,code,open,high,low,close,volume,amount",
                                          start_date=start_date, end_date=end_date,
                                          frequency=frequency, adjustflag="2")
        data_list = []
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        result['time'] = result['time'].apply(lambda x: make_datetime_str(x))
        result = result.rename(columns={'time': 'datetime'})
        if update: #每日更新
            # with open(file_path + stock_code_ + '.csv', 'a') as f:
            #     f.write('\n')
            result = cut_min_repeated_row(file_path + stock_code_ + '.csv', result)
            result.to_csv(
                file_path + stock_code_ + '.csv',
                index=False,
                mode='a',
                header=False,

            )
        else: #直接保存
            result.to_csv(file_path + stock_code_ + '.csv', index=False)
        print(" 国内分钟完成:",stock_code_ )
        # print('进度:  %4.2f' % ((self.index(stock) + 1) / len(self.stock_list)))
    print('------------------国内分钟成功---------------------------')


import  threading

def run():
    start = time.time()
    today_date = get_today_date()
    CN_list = china_all_stock_list
    bs.login()
    # 国内股票

    # get_china_stock_day_data(stock_list= CN_list,
    #                                   start_date='2006-01-01',
    #                                   end_date=today_date,
    #                                  file_path=china_stock_day_file_path,
    #                                   update=False
    #                                   )
    #
    # # 获取国内股票15min
    # get_china_stock_min__data(stock_list= CN_list,
    #                                    start_date='2015-01-01',
    #                                    end_date=today_date,
    #                                    file_path=china_stock_min_file_path,
    #                                    update= False)
    #
    a = 0
    for i in CN_list:
        name = str(i)+'day'
        thr = threading.Thread(target=get_china_stock_day_data,
                               args=(i, '2006-01-01', today_date, china_stock_day_file_path, False, "d"),
                               name=name)
        thr.start()
        # print("线程id: 日线{},代码{}".format(threading.current_thread().name, i))
        thr_min = threading.Thread(target=get_china_stock_min__data,
                                   args=(i, '2015-01-01', today_date, china_stock_min_file_path, False, '15'),
                                   name=str(i)+'min')
        thr_min.start()
        if threading.active_count()>16:
            time.sleep(5)
        print("线程id: 个数: {},代码: {}".format(threading.active_count(), i))
        a +=1
    bs.logout()
    end = time.time()
    print('总耗时：%s' % (end - start))

run()