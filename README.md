# 获取某年的除息除权日期

如果pip运行的路径不对。运行一下命令hash -r

# 顺序运行steps, 官方要求别同时运行多线程或多进程下载数据。
1. python3 trade_dates.py  
2. python3 stock_basic.py  
3. python3 dividend.py 2020 有时会失败
4. python3 dividend_preclose.py  有时会失败， 多运行几次, 有时慢得要命
