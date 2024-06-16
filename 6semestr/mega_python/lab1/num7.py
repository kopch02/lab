import datetime as dt
import schedule


def job(st="ку", time=None):
    hour = dt.datetime.now().hour
    if time != None:
        start, end = map(int, time)
        if hour > start and hour < end:
            return
    print(st * int(hour))


string = input("string -->")
time_start = input("time start-->")
time_end = input("time end-->")
schedule.every().hour.at(":00").do(job, st=string, time=[time_start, time_end])

while True:
    schedule.run_pending()