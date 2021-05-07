import threading
from concurrent.futures import ThreadPoolExecutor,as_completed
import datetime

import pandas as pd
import pymysql
from sqlalchemy import create_engine
import baostock as bs

DB_CONFIG= {
"host": '127.0.0.1',
"user" :'root',
"passwd":'5279888' ,
"port":3306,
"db":'china_stock',
"charset":'utf8'


}
CHINA_STOCK_ENGIN = create_engine("mysql+mysqldb://root:5279888@127.0.0.1/china_stock",encoding='utf8')


baostock_day_k_fields = ','.join(["date","code","open","high","low","close","preclose","volume","amount",
                                  "adjustflag","turn",'tradestatus','pctChg','isST'])

class SaveDate(object):
    def __init__(self,db_config,table_name):
        self.db_config= db_config
        self.conn=pymysql.connect(**self.db_config)
        self.cusor=self.conn.cursor()
        self.table_name=table_name

    def create_table(self):
        self.cusor.execute(
            '''
        CREATE TABLE IF NOT EXISTS `{}`(
           `id` INT UNSIGNED AUTO_INCREMENT,
           `code` VARCHAR(100) NOT NULL,
           `date` varchar (100),
           `open`  varchar (100),
           `high`  varchar (100),
           `low`  varchar (100),
           `close`  varchar (100),
           `preclose`  varchar (100),
           `volume`  varchar (100),
           `amount`  varchar (100),
           `adjustflag`  varchar (100) ,
           `turn`  varchar (100) ,
           `tradestatus`  varchar (100) ,
           `pctChg`  varchar (100) ,
           `isST`  varchar (100) ,
           PRIMARY KEY ( `id` )
        )ENGINE=InnoDB DEFAULT CHARSET=utf8;

            '''.format(self.table_name)
        )
        self.conn.commit()

    def save_data_to_mysql(self,data):
        self.cusor.execute(
            '''
        INSERT INTO TABLE  `{}`( code, date,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,
        pctChg,isST)
                       VALUES
                       ( value1, value2,...valueN );
        
            '''.format(self.table_name)
        )
        self.conn.commit()



    def exist_in_table(self,data):
        self.cusor.execute(
            " SELECT * FROM {} WHERE code='{}' AND  `date`='{}'".format(self.table_name,data['code'],data['date'])
        )

        num=self.cusor.fetchall()
        if num:
            return True
        else:
            return False
    def get_mysql_last_day(self,code):
        print(self.table_name,code)
        print(type(self.table_name),type(code))
        self.cusor.execute(
             " SELECT date FROM {} WHERE code='{}' order by date desc  limit 1".format(self.table_name,code)
        )

        num=self.cusor.fetchall()
        print(num)
        if num:
            return num[0][0]
        else:
            return None
    def get_today_date(self):
        # 2014-01-01
        today = datetime.date.today().strftime('%Y-%m-%d')
        return today

    def fomate_date(self,date_tuple:tuple)->str:
        date = datetime.date(year=date_tuple[0],month=date_tuple[1],day=date_tuple[2]).strftime('%Y-%m-%d')
        print(type(date))
        print(date)
        return date


    #获取股票列表
    def get_all_china_stock_list(self):
        stock_rs = bs.query_all_stock("2019-02-25")
        stock_df = stock_rs.get_data()
        return stock_df['code']

    def get_data_from_baostock_first_time( self,start_time,end_time,stock_list):
        # stock_list = ['sh.000001']
        for stock in stock_list:
            last_day = self.get_mysql_last_day(stock)
            print('{}开始的时间:{}'.format(stock,last_day))

            day_data = bs.query_history_k_data_plus(code=stock,fields=baostock_day_k_fields,
                                                       start_date=last_day,end_date=end_time,
                                                      frequency='d',adjustflag='1')
            if day_data.error_code !='0':
                print('========={} 出错============'.format(stock))

            data_df= day_data.get_data()
            today_data = data_df.iloc[-1,:]
            if self.exist_in_table(today_data):
                print('{}已保存'.format(stock))
                continue
            for index, row in data_df.iterrows():
                if self.exist_in_table(row):
                    data_df = data_df.drop(index=[index,])
            # data_df[['open', 'high','low','close','preclose','volume','amount','',]] = data_df[['col2', 'col3']].apply(
            #     pd.to_numeric)

            data_df.to_sql(name=self.table_name,con=CHINA_STOCK_ENGIN,if_exists='append',index=False)
            print('{}保存成功'.format(stock))


if __name__ == '__main__':
    bs.login()

    china_Stoc_day = SaveDate(db_config=DB_CONFIG,table_name='china_stock_day')
    china_Stoc_day.create_table()
    china_Stoc_day.get_all_china_stock_list()

    china_Stoc_day.get_data_from_baostock_first_time(start_time=china_Stoc_day.fomate_date((1990,12,19)),
                                          end_time=china_Stoc_day.get_today_date(),stock_list=china_Stoc_day.get_all_china_stock_list())


    bs.logout()

