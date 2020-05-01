#for((i=172;i<=244;i++));  
#do   
## echo `date -d "$i month ago" '+%Y%m'`
#python3 download_daily.py `date -d "$i month ago" '+%Y%m'`
#done

python3 download_daily.py `date +'%Y%m'`   # 下载当月
python3 download_daily.py `date -d '1 month ago' '+%Y%m'`   # 下载上个月

