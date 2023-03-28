#from Cron_Util import Cron_Util
from activity import activity
from time import time
from datetime import datetime
from MARSFarm_Util import *

from Time_Util import get_time_str

class Activity(object):
    
    def __init__(self):
        self.activity = activity

    def set_exp_name(name):
        self.activity[EXPERIMENT][NAME] = name

    def set_exp_id(id):
        self.activity[EXPERIMENT][ID] = id

    def set_trial_name(name):
        self.activity[TRIAL][NAME] = name

    def set_trial_id(id):
        self.activity[TRIAL][ID] = id
        
    def set_start_date(timestamp):
        self.activity[TIME][TIMESTAMP] = timestamp
        self.activity[TIME][TIME_STR] = get_time_str(timestamp)

def test():
    print("Trial Object Test")
    t = Trial()
    t.pretty_print()
    print('Trial Id:', t)
    print('Trial Name:', t.trial_name)
    print("Start Date", t.start_date)
    print("Done")
    
if __name__=="__main__":
    test()
