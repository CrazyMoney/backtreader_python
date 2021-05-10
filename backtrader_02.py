import json

import baostock as bs
from backtrader import feed
import backtrader as bt
import pyfolio as pf
import pandas

baostock_day_k_fields = ','.join(["date","code","open","high","low","close","preclose","volume","amount",
                                  "adjustflag","turn",'tradestatus','pctChg','isST'])
<<<<<<< HEAD
import akshare as ak


def get_stock_zh_day():
    # stock_zh_a_daily_qfq_df = ak.stock_zh_a_daily(symbol="sz000002", start_date="20101103", end_date="20201116",
    #                                               adjust="qfq")

    stock_zh_a_spot_df = ak.stock_zh_a_spot()
    print(stock_zh_a_spot_df)
    stock_list= stock_zh_a_spot_df['代码'].tolist()
    print(stock_list)
    print(type(stock_list))
    stock_list_str =  json.dumps(stock_list).encode(encoding='utf8')
    print(stock_list_str)
    print(type(stock_list_str))
    with open('./all_cn_stocks','wb')  as f :
        f.write(stock_list_str)
    # print(stock_zh_a_daily_qfq_df)


def get_data_from_baostock_first_time(stock):
    # stock_list = ['sh.000001']
    stock = 'sz.002241'
    stock = stock
    all_stocks = bs.query_all_stock()
    stock_df = all_stocks.get_data()
    print(stock_df.head())
=======
import  akshare as ak

def get_all_stock():
    all_stock = ak.stock_zh_a_spot()
    print(all_stock)
    print(type(all_stock))
    stock_list = all_stock['代码'].tolist()
    stock_str = json.dumps(stock_list,ensure_ascii=False)
    with open('all_china_stocks.txt','w')as f :
        f.write(stock_str)






def get_data_from_baostock_first_time(stock):
    # stock_list = ['sh.000001']
    # stock = 'sz.002241'


>>>>>>> 2e73c09a932b538c4a4ea67e150d3bee4371bf54
    day_data = bs.query_history_k_data_plus(code=stock, fields=baostock_day_k_fields,
                                            start_date='2019-01-01', end_date="2021-04-28",
                                            frequency='d', adjustflag='1')

    data_df = day_data.get_data()
    return  data_df
    # print('{}保存成功'.format(data_df))

class my_strategy1(bt.Strategy):
    #全局设定交易策略的参数
    params=(
        ('maperiod',5),
           )
    def __init__(self):
        #指定价格序列
        self.dataclose=self.datas[0].close
        print(self.datas)
        # 初始化交易指令、买卖价格和手续费
        self.order = None
        self.buyprice = None
        self.buycomm = None

        #添加移动均线指标，内置了talib模块
        self.sma = bt.indicators.SimpleMovingAverage(
                      self.datas[0], period=self.params.maperiod)
    def next(self):
        if self.order: # 检查是否有指令等待执行,
            return
        # 检查是否持仓
        if not self.position: # 没有持仓
            #执行买入条件判断：收盘价格上涨突破20日均线
            if self.dataclose[0] > self.sma[0]:
                #执行买入
                self.order = self.buy(size=500)
        else:
            #执行卖出条件判断：收盘价格跌破20日均线
            if self.dataclose[0] < self.sma[0]:
                #执行卖出
                self.order = self.sell(size=500)

class MyPandasData(bt.feeds.PandasData):
    params = (

        # Possible values for datetime (must always be present)
        #  None : datetime is the "index" in the Pandas Dataframe
        #  -1 : autodetect position or case-wise equal name
        #  >= 0 : numeric index to the colum in the pandas dataframe
        #  string : column name (as index) in the pandas dataframe

        # Possible values below:
        #  None : column not present
        #  -1 : autodetect position or case-wise equal name
        #  >= 0 : numeric index to the colum in the pandas dataframe
        #  string : column name (as index) in the pandas dataframe
        ('datetime', 'date'),
        ('nocase', True),
        ('open', 'open'),
        ('high', 'high'),
        ('low', 'low'),
        ('close', 'close'),
        ('volume', 'volume'),
        ('openinterest', 'openinterest'),
    )

    datafields = [
        'date', 'open', 'high', 'low', 'close', 'volume', 'openinterest'
    ]

    def __init__(self):
        super().__init__()



def runstrat(dataframe):

    dataframe[['open','high','low','close','preclose','volume','amount','adjustflag','turn','tradestatus','pctChg','isST']]= dataframe[['open','high','low','close','preclose','volume','amount','adjustflag','turn','tradestatus','pctChg','isST']].apply(pandas.to_numeric)
    dataframe['openinterest']= 0
    dataframe['date']= pandas.to_datetime(dataframe['date'])
    cerebro = bt.Cerebro()
    cerebro.addstrategy(my_strategy1)
    data = MyPandasData(dataname=dataframe)
    cerebro.adddata(data)
    cerebro.adddata(data)
    cerebro.broker.setcash(1000000)
    cerebro.broker.setcommission(commission=0.002)
    # cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')
    cerebro.run()
    portvalue = cerebro.broker.getvalue()
    print('总资金:{}'.format(portvalue))


def translate_df(dataframe):
    dataframe[['open','high','low','close','preclose','volume','amount','adjustflag','turn','tradestatus','pctChg','isST']]= dataframe[['open','high','low','close','preclose','volume','amount','adjustflag','turn','tradestatus','pctChg','isST']].apply(pandas.to_numeric)
    dataframe['openinterest']= 0
    dataframe['date']= pandas.to_datetime(dataframe['date'])
    return  dataframe


if __name__ == '__main__':
    bs.login()
<<<<<<< HEAD
    # get_stock_zh_day()
    with open('./all_cn_stocks','rb')  as f :
        stock_str = f.read()
        stock_list = json.loads(stock_str.decode(encoding='utf8'))
        print(stock_list)
    for stock in stock_list:
        stock_str = stock[:2] + '.' + stock[2:]
        print(stock_str)
        # df = get_data_from_baostock_first_time(stock_str)
        bs.logout()
=======
    sh_index = 'sh.000001'
    sz_index = 'sz.399106'
    sh_list= []
    sz_list = []
    with open('all_china_stocks.txt','r')as f:
        content = f.read()
        stock_list = json.loads(content)
        for stock in stock_list:
            if stock.startswith('sh'):
                sh_list.append(stock[:2] + '.'+ stock[2:])
            else:
                sz_list.append(stock[:2] + '.'+ stock[2:])
    #下载数据
    # for sh_stock in sh_list:
    #     df = get_data_from_baostock_first_time(sh_stock)
    #     df.to_csv('./csv/'+sh_stock+'.csv',mode='w')
    # df = get_data_from_baostock_first_time(sh_index)
    # df.to_csv('./csv/'+sh_index+'.csv',mode='w')
    # df = get_data_from_baostock_first_time(sz_index)
    # df.to_csv('./csv/'+sz_index+'.csv',mode='w')
    #
    #

    new_df = pandas.DataFrame()
    sh_index_df = pandas.read_csv('./csv/'+sh_index+'.csv')
    new_df['sh_index_turn'] = sh_index_df['turn'].apply(pandas.to_numeric)

    for sh_stock in sh_list[::50]:
        df = pandas.read_csv('./csv/'+sh_stock+'.csv')
        new_df['sh_index_turn'] = sh_index_df['turn'].apply(pandas.to_numeric)
        new_df[sh_stock] = df['turn'].apply(pandas.to_numeric)
    print(new_df.head())
    print(new_df.corr())

    corr = new_df.corr().sort_values(by='sh_index_turn')
    print(corr)










    # df = get_data_from_baostock_first_time()
    bs.logout()
    # get_all_stock()
>>>>>>> 2e73c09a932b538c4a4ea67e150d3bee4371bf54
    # runstrat(df)

