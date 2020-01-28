from datetime import date
from datetime import datetime
a = date.today()
b = datetime.now()

def current_date():
    day = a.strftime("%Y/%m/%d")
    return day

def current_time():
    now = b.strftime("%H:%M:%S")
    return now
