import datetime as dt
import schedule


def job():
    time = dt.datetime.now()
    time = time.hour % 12
    print("ку " * int(time))


schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()