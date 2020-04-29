import baostock as bs
import pandas as pd

def today():
    import datetime
    print (datetime.datetime.now().strftime("%Y-%m-%d"))
    
#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取交易日信息 ####
rs = bs.query_trade_dates(start_date="2006-01-01", end_date=today())
print('query_trade_dates respond error_code:'+rs.error_code)
print('query_trade_dates respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

result.to_csv("/home/toby/data/datasource/baostock/trade_dates.csv", encoding="gbk", index=False )
# print(result)

#### 登出系统 ####
bs.logout()
