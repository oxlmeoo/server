from datetime import datetime
import time
import os
import job2
from apscheduler.triggers import interval
from apscheduler.schedulers.background import BackgroundScheduler
  
  
def tick():
    job2.job()
if __name__ == '__main__':
 scheduler = BackgroundScheduler()
 trigger = interval.IntervalTrigger(seconds=1800)
 now = int(time.time())
 timeArray = time.localtime(now)
 otherStyleTime = time.strftime("%Y%m%d %H:%M:%S", timeArray)
 scheduler.add_job(tick,trigger=trigger, id='status_update_job', replace_existing=True)
 print(otherStyleTime+ '创建任务半小时执行一次')
 scheduler.start()
 try:
  # This is here to simulate application activity (which keeps the main thread alive).
  while True:
   time.sleep(2)
 except (KeyboardInterrupt, SystemExit):
  scheduler.shutdown() # Not strictly necessary if daemonic mode is enabled but 