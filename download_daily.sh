#for((i=172;i<=244;i++));  
#do   
## echo `date -d "$i month ago" '+%Y%m'`
#python3 download_daily.py `date -d "$i month ago" '+%Y%m'`
#done

# 如果没有当月文件，就下载上个月数据。
date=`date +'%Y%m'`
[ ! -e "/home/toby/data/datasource/baostock/daily/$date.csv" ] && python3 download_daily.py `date -d '1 month ago' '+%Y%m'`   # 下载上个月

python3 download_daily.py `date +'%Y%m'`   # 下载当月

