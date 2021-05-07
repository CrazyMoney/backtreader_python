import baostock as bs

from data.BackTreder_get_Data import GetDataFromBaoStock, GetDataFromSina, GetDateFromYahoo
from utils import get_today_date, get_n_days_ago_date
from  settings import  (
                        china_all_stock_list,
                        china_furture_min_file_path,
                        china_furture_day_file_path,
                        china_stock_min_file_path,
                        china_stock_day_file_path,
                        China_fu_list,
                        UsStock_list,
                        us_stock_min_file_path,
                        us_stock_day_file_path
                        )


if __name__ == '__main__':

    today_date = get_today_date()

    #国内股票
    lg = bs.login()
    baostock = GetDataFromBaoStock(3, today_date,china_all_stock_list)
    baostock.get_china_stock_day_data(frequency='d', start_date=today_date,
                                  end_date=today_date,update=True,file_path=china_stock_day_file_path)  # 更新国内日线数据
    baostock.get_china_stock_min__data(frequency='15',start_date=today_date,end_date= today_date,file_path=china_stock_min_file_path,update=True) # 更新国内日线数据

    bs.logout()

    #国内期货
    sina_ = GetDataFromSina(China_fu_list)
    sina_.get_cn_furture_day(china_furture_day_file_path)
    sina_.get_cn_furture_min(china_furture_min_file_path)


    #美股更新
    yesterday_ = get_n_days_ago_date(1)
    two_day_ago = get_n_days_ago_date(2)
    yahoo_ = GetDateFromYahoo(UsStock_list)
    yahoo_.get_us_stock_day(file_path=us_stock_day_file_path,update=True,period='5d',interval='id')
    yahoo_.get_us_stock_min(file_path=us_stock_min_file_path,update=True,start=two_day_ago,end=today_date,interval='5m')
