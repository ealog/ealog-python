import datetime
import time

cur_time_minute = datetime.datetime.now().minute
cur_time_second = datetime.datetime.now().second

if cur_time_minute == 0 or cur_time_minute == 30:
    sleep_time=0
elif cur_time_minute < 30:
    sleep_time = (30-cur_time_minute)*60 - cur_time_second
elif cur_time_minute > 30:
    sleep_time = (60-cur_time_minute)*60 - cur_time_second
print(sleep_time)
time.sleep(sleep_time)



while True:
    hour_now=datetime.datetime.now().hour
    minute_now=datetime.datetime.now().minute
    print(hour_now)
    print(minute_now)
    
    minute_now=datetime.datetime.now().minute
    second_now=datetime.datetime.now().second
    
    if sleep_time == 0 and (minute_now == 1 or minute_now == 31):
        a = 1
        time.sleep(a)
        print(a)
    else:
        b = 2
        time.sleep(b)
        print(b)
