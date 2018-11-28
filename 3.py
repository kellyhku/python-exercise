import datetime 
import time 
while(True): 
  s = raw_input('请输入日期:(格式为“2012-01-01”,输入“No”终止程序)\n') 
    while(str!='No'): 
      date_time=time.strptime(s,"%Y-%m-%d") 
      yWeek=time.strftime("%W",date_time) 
      intYweek=int(yWeek) 
      print date_time.tm_yday,'',intYweek 
      break 
    else: 
      print '程序终止！' 
      break
