from datetime import datetime
import time
import schedule


def sayHello():
    now = datetime.now()
    print(f'固定美十秒鐘: {now}')


schedule.every(10).seconds.do(sayHello)
#.unit("24:00")

while True:
    schedule.run_pending()
    time.sleep(1)
