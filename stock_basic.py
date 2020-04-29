import baostock as bs
import pandas as pd

#### 得到所有的股票代码code
import pandas as pd
code = []
data = pd.read_csv('/home/toby/data/sz_code.csv',encoding='utf-8',header=None)
code.extend(data[0].values.tolist()) 
data = pd.read_csv('/home/toby/data/sh_code.csv',encoding='utf-8',header=None)
code.extend(data[0].values.tolist()) 

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)


data_list = []
for sym in code:
    # 获取证券基本资料
    rs = bs.query_stock_basic(code=sym)
    # rs = bs.query_stock_basic(code_name="浦发银行")  # 支持模糊查询
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
        
result = pd.DataFrame(data_list, columns=rs.fields)
result.to_csv("/home/toby/data/datasource/baostock/stock_basic.csv", encoding="gbk", index=False)

bs.logout()

```
返回数据说明
参数名称	参数描述
code	证券代码
code_name	证券名称
ipoDate	上市日期
outDate	退市日期
type	证券类型，其中1：股票，2：指数,3：其它
status	上市状态，其中1：上市，0：退市
```
