from MongoUtil import MongoUtil
from trial import trial
from MARSFarm_Util import *
from config import DB, OBSV_COL
from datetime import datetime

class LightUtil(object):
    
    def __init__(self):
        self._mu = MongoUtil()
        self._trial_id = trial[ID]

    def get_last_light(self):
        query = {"trial.id":self._trial_id, "subject.name":LIGHT, "subject.attribute.name":DURATION}
        #query = {"trial.id":self._trial_id, "subject.name":LIGHT}
        doc = self._mu.get_last(DB, OBSV_COL, query)
        if doc is None:
            print("No light doc")
            return None, None
        elif doc[STATUS][STATUS] != IN_PROCESS:
            # fail to have recorded light on event
            print("No light on event")
            return None, None
        return doc["_id"], doc[TIME][TIMESTAMP]
        
    def update_light(self, id, start):
        # Find last light-on record and update it with duration and end_time
        
        # end_date
        ts = datetime.now().timestamp()
        end_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # look for last light_on record
        id, timestamp = self.get_last_light()
        if id is None:
            # if no record, exit
            return None
        
        min = self.minutes(start, ts)
        
        # create update
        match  = {"_id":id}
        update = { "$set":{"status.status":COMPLETE, "status.status_qualifier":SUCCESS, "subject.attribute.value":min, "time.end_date":ts, "time.end_date_str":end_str}}
        self._mu.update(DB, OBSV_COL, match, update)
        #print(match)
        #print(update)
        
    def minutes(self, start, end):
        # calculate minutes between two timestamps
        return (end - start)/60
    
def test():
    print("Light Query Test")
    lu = LightUtil()
    print("Get Last")
    id, ts = lu.get_last_light()
    print("ID", id, "Time", ts)
    print("Update")
    lu.update_light(id, ts)
    print("Done")
    
if __name__=="__main__":
    test()
    