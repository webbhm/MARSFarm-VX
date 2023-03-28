'''
Abstracts saving to hide loctions and number if instances
Defaults to must MongoDB for Observations
Wrapper for S3 image handling
Author: Howard Webb
Date: 2023-2-11
'''
from MongoUtil import MongoUtil
from config import URL, DB, OBSV_COL
from MARSFarm_Util import LOCATION, FIELD, ID
from location import location


class Saver(object):
    
    def __init__(self):
        self.con = MongoUtil()
        
    def save_Obsv(self, msg):
        print(msg)
        return self.con.insert_one(DB, OBSV_COL, msg)
    
    def update_light(self, update):
        # update the latest light duration record with duration value
        field_id = location[FIELD][ID]
        match = {'subject.attribute.name':'Duration', 'location.field.id':field_id}
        doc = self.con.get_last(DB, OBSV_COL, match)
        find = {'_id':doc['_id']}
        return self.con.update(DB, OBSV_COL, find, update)
        