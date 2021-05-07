import  pandas as pd




from  settings import (

china_stock_day_file_path,
china_stock_min_file_path,
us_stock_day_file_path,
us_stock_min_file_path,
UsStock_list,
Chine_stock_list,
)
def get_data_from_csv(file_path,stock_list):
    stock_data_list =[]
    for s in stock_list:
        df = pd.read_csv(file_path+s+".csv")
        stock_data_list.append(df)
    return stock_data_list
def get_chinda_stcok_day_data_form_csv():
    return get_data_from_csv(china_stock_day_file_path,Chine_stock_list)
def get_china_stock_min_from_csv():
    return  get_data_from_csv((china_stock_min_file_path,Chine_stock_list))
def get_us_stock_day_from_csv():
    return get_data_from_csv(us_stock_day_file_path,UsStock_list)
def get_us_stock_min_from_csv():
    return get_data_from_csv(us_stock_min_file_path,UsStock_list)