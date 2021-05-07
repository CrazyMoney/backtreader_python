# s= '20150105094500000'
# y,m,d,h,mi,s = s[0:4],s[4:6],s[6:8],s[8:10],s[10:12],s[12:14]
# datetime_str = y+'-'+m+'-'+d+' '+d+":"+mi+":"+s
# print(datetime_str)

#废弃
# class GetDateFromPandas():
    # def __init__(self,us_stock_list):
    #     self.stock_list = us_stock_list
    # def get_us_stock_day(self):
    #     stock_dir ={}
    #     for s in self.stock_list:
    #         stock_dir[s] = web.get_data_yahoo(s,start='2020-06-01',end = '2020-06-15')
    #     for key,values in stock_dir.items():
    #         print(values.head(10))


#废弃
# class GetDataFromTDX():
#     '''
#   market  category      name short_name
#   1         1       临时股         TP
#   4        12    郑州商品期权         OZ
#   5        12    大连商品期权         OD
#   6        12    上海商品期权         OS
#   7        12     中金所期权         OJ
#   8        12    上海股票期权         QQ
#  28         3      郑州商品         QZ
#  29         3      大连商品         QD
#  30         3      上海期货         QS
#  37        11  全球指数(静态)         FW
#  42         3      商品指数         TI
#  43         1     B股转H股         HB
#  44         1      股转系统         SB
#  45         6     OTC市场         OT
#  46        11      上海黄金         SG
#  47         3     中金所期货         CZ
#  50         3      渤海商品         BH
#  60         3    主力期货合约         MA
#  62         5      中证指数         ZZ
#  71         2       港股通         GH
#  76         3      齐鲁商品         QL
# 102         5      国证指数         GZ
#
#     '''
#     def __init__(self,stock_best_ip,future_best_ip):
#         self.stock_best_ip = stock_best_ip
#         self.future_best_ip = future_best_ip
#
#     def get_cn_furture_day(self):
#         api = TdxExHq_API()
#         with api.connect(self.future_best_ip["ip"], int(self.future_best_ip['port'])):
#             # print(api.to_df( api.get_markets()))
#             df =  api.to_df(api.get_instrument_info(0,22047))
#             df1 = df.loc[df['market']==29]
#             print(df1)
#             # pprint.pprint(api.to_df(api.get_instrument_bars(TDXParams.KLINE_TYPE_DAILY, 8, "10000843", 0, 100)))

#废弃
# class GetFromTushare():
#     def __init__(self,apikey='c70d79c6663a747b1c45416b02c0529b046a363c8d35faea73c6b19f'):
#          self.pro = ts.pro_api(apikey)
#     def get_cn_furtuer_data(self,furtuer_list):
#         '''
#         交易所代码 CFFEX-中金所 DCE-大商所 CZCE-郑商所 SHFE-上期所 INE-上海国际能源交易中心
#         合约类型 (
#                 1 普通合约
#                 2主力与连续合约
#                  默认取全部)
#         '''
#
#         all_furture =  self.pro.fut_basic(exchange='DCE', fut_type='1', fields='ts_code,symbol,name,list_date,delist_date')
#         print(all_furture)

s1 ='2020-05-29 15:55:00-04:00'
s2 = s1[:-6]
print(s2)