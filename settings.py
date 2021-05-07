from utils import get_all_cn_stocks__from_csv

project_path = '/Users/zheng/Desktop/csv_data/'
csv_file_path = '/Users/zheng/Desktop/csv_data/stocks_furtures/'  #存储所有code 列表的


#国内股票配置
china_all_stock_list = get_all_cn_stocks__from_csv()
Chine_stock_list = get_all_cn_stocks__from_csv()
china_stock_day_file_path = project_path+"china_stocks_day_file/"
china_stock_min_file_path = project_path+"china_stocks_min_file/"

#国内期货配置
China_fu_list =['a2009','c2009','m2009','jd2009','rb2010','i2009','sc2008','ma2009']
china_furture_day_file_path = project_path+"china_future_day_file/"
china_furture_min_file_path = project_path+"china_future_min_file/"


#美国股票配置
UsStock_list = ['UCO', 'JD', 'BIDU', 'PG', 'TSLA', 'ZM', 'NFLX', 'GILD','UVXY'
                ,'BABA', 'SINA', 'IRBT', 'SBUX', 'SNE',
                'AMZN', 'MSFT', 'NTES', 'AAPL',  'SLV', 'NEW', 'BILI',
                'MU', 'EWI', 'MCD', 'EUO','GOOG', 'SGMS', 'TEO',
                'IQ', 'WB', 'FB', 'FDX', 'KO', 'PEP', 'RACE', 'F']
us_stock_day_file_path = project_path+"us_stocks_day_file/"
us_stock_min_file_path = project_path+"us_stocks_min_file/"





