import baostock as bs
import pandas as pd

print("python dividend_preclose.py year\n")
import sys
year =sys.argv[1]

#### 得到所有的股票代码code
import pandas as pd
dividend = pd.read_csv('/home/toby/data/datasource/baostock/dividend_' + year + '.csv',encoding='utf-8')
trade_day = pd.read_csv('/home/toby/data/datasource/baostock/trade_dates.csv',encoding='utf-8')
trade_day_dict = dict( (name,value) for name,value in zip(trade_day['calendar_date'],trade_day['is_trading_day']))
def nextday(date):
    keys = list(trade_day_dict.keys())
    if not date in keys:
        return None
    index = keys.index(date)
    if len(keys) == index+1: # 最后一个
        return None
    date = keys[index+1]
    while '0' == trade_day_dict[date]:
        if len(keys) == index+1: # 最后一个
            return None
        date = keys[index+1]
    return date

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

data_list = []
for index, row in dividend.iterrows():
    code = row['code']
    print(code)
    date = row['dividOperateDate']
#### 获取沪深A股历史K线数据 ####
    istradeday = False
    while not istradeday:
        # print(date)
        rs = bs.query_history_k_data_plus(code,
            "date,code,close,preclose, tradestatus",
            start_date=date, end_date=date,
            frequency="d", adjustflag="3")
        while (rs.error_code == '0') & rs.next():
            # print("received one")
            # 获取一条记录，将记录合并在一起
            row_data = rs.get_row_data()
            if '1'==row_data[4]: #正常交易日,没停牌
                istradeday = True
                data_list.append(row_data)
        date = nextday(date)
        if date == None:  #到达最后一天
            istradeday = True         
            
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####   
result.to_csv("/home/toby/data/datasource/baostock/dividend_preclose_" + year + ".csv", index=False)
# print(result)

#### 登出系统 ####
bs.logout()

