import time
from datetime import datetime, timedelta

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

now = datetime.now()
print(now)
print(now.strftime("%m.%d, %Y"))
y = datetime.now().year
m = datetime.now().month
d = datetime.now().day

print(f'{y}년 {m}월 {d}일')

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(f'{yesterday} - {today} - {tomorrow}')

date1 = datetime(2024, 12, 5)
date2 = datetime(2023, 10, 7)
diff = date1 - date2
print(diff)


sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1
    