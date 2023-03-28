'''
Time calculations
Author: Howard Webb
Date: 2/9/2023
'''

from datetime import datetime
import time
import math
from MARSFarm_Util import *

def get_day(start_date):
    # calculate number of days since start_date (as timestamp)
    now = datetime.now().timestamp()
    dif = now - start_date
    days = math.ceil(dif/(60*60*24))
    return days
    
def get_week(start_date):
    # calaculate number of weeks since start_date
    days = get_day(start_date)
    weeks = math.ceil(days/7)
    return weeks

def get_time_struct(start_date):
    # build record time structure, start_time is None if not in trial
    ts = datetime.now().timestamp()
    tstr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if start_date is not None:
        time = {TIMESTAMP:ts, TIME_STR:tstr, DAY:get_day(start_date), WEEK:get_week(start_date)}
    else:
        time = {TIMESTAMP:ts, TIME_STR:tstr}
    return time
    
def get_time_str(timestamp):    
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")
    
def test():
    print("Time Util Test")
    start_date = datetime.strptime("2023-1-2", "%Y-%m-%d").timestamp()
    print("Day", get_day(start_date))
    print("Week", get_week(start_date))
    print(start_date, get_time_struct(start_date))
    print("None", get_time_struct(None))
    print("Time Str", get_time_str(time.time()))
    print("Done")
    
if __name__=="__main__":
    test()
