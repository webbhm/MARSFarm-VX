'''
Abstracts saving to hide loctions and number if instances
Defaults to must MongoDB for Observations
Wrapper for S3 image handling
Author: Howard Webb
Date: 2023-2-11
'''
from MongoUtil import MongoUtil
from config import URL, DB, OBSV_COL

class Saver(object):
    
    def __init__(self):
        self.con = MongoUtil()
        
    def save_Obsv(self, msg):
        print(msg)
        return self.con.insert_one(DB, OBSV_COL, msg)
        