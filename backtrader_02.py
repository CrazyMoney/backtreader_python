

import baostock as bs
from backtrader import feed
import backtrader as bt
import pyfolio as pf
import pandas

baostock_day_k_fields = ','.join(["date","code","open","high","low","close","preclose","volume","amount",
                                  "adjustflag","turn",'tradestatus','pctChg','isST'])

def get_data_from_baostock_first_time():
    # stock_list = ['sh.000001']
    stock = 'sz.002241'

    day_data = bs.query_history_k_data_plus(code=stock, fields=baostock_day_k_fields,
                                            start_date='2020-01-01', end_date="2021-04-28",
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




if __name__ == '__main__':
    bs.login()
    df = get_data_from_baostock_first_time()
    bs.logout()
    runstrat(df)

