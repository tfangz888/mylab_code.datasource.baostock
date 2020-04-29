import baostock as bs
import pandas as pd

print("python dividend.py year\n")
import sys
year =sys.argv[1]

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 得到所有的股票代码code
import pandas as pd
code = []
data = pd.read_csv('/home/toby/data/sz_code.csv',encoding='utf-8',header=None)
code.extend(data[0].values.tolist()) 
data = pd.read_csv('/home/toby/data/sh_code.csv',encoding='utf-8',header=None)
code.extend(data[0].values.tolist()) 

#### 查询除权除息信息####
# 查询某年除权除息信息
rs_list = []
for sym in code:
    rs_dividend = bs.query_dividend_data(code=sym, year=year, yearType="report")
    while (rs_dividend.error_code == '0') & rs_dividend.next():
        rs_list.append(rs_dividend.get_row_data())

result_dividend = pd.DataFrame(rs_list, columns=rs_dividend.fields)

#### 结果集输出到csv文件 ####   
result_dividend.to_csv("/home/toby/data/datasource/baostock/dividend_" + year + ".csv", encoding="gbk",index=False, columns=['code', 'dividOperateDate'])

#### 登出系统 ####
bs.logout()
