import baostock as bs
import pandas as pd

print("python download_daily.py 201908")
import sys
date = sys.argv[1]

date1 = date[0:4] + '-' + date[4:6] + '-01'
from datetime import datetime
from dateutil.relativedelta import relativedelta
date1 = datetime.strptime(date1, '%Y-%m-%d') # 开始日期
date2 = date1 + relativedelta(months=1)    # 结束日期
if date2 > datetime.now():
    date2 = datetime.now()
date1 = date1.strftime('%Y-%m-%d')
date2 = date2.strftime('%Y-%m-%d')

#### 得到所有的股票代码code
import pandas as pd
code = []
data = pd.read_csv('/home/toby/data/sz_code.csv',encoding='utf-8',header=None)
code.extend(data[0].values.tolist()) 
data = pd.read_csv('/home/toby/data/sh_code.csv',encoding='utf-8',header=None)
code.extend(data[0].values.tolist()) 

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

data_list = []
for sym in code:
    print (sym)
    #### 获取历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节
    rs = bs.query_history_k_data_plus(sym,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
        start_date=date1, end_date=date2, 
        frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
    
    #### 打印结果集 ####    
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        one_record = rs.get_row_data()
        if '1' == one_record[11]:  # 只存交易日数据
            data_list.append(one_record)
if len(data_list) > 0:
    result = pd.DataFrame(data_list, columns=rs.fields)
    #### 结果集输出到csv文件 ####
    result.to_csv("/home/toby/data/datasource/baostock/daily/" + date + ".csv", encoding="gbk", index=False)

#### 登出系统 ####
bs.logout()
