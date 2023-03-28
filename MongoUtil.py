'''
A group of MongoDB functions to demonstrate and test query capabilities.
This generates the data needed to populate the Fairchild spreadsheet from data sources

Author: Howard Webb
Date: 6/29/2021
'''

from pymongo import MongoClient
import dns.resolver
from pprint import pprint
import json
from datetime import datetime
# not used
from bson.json_util import dumps, loads
from config import *

from MARSFarm_Util import *

# logon string to get into the database

class MongoUtil(object):
    
    def __init__(self):
        # Create a database client
        dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
        dns.resolver.default_resolver.nameservers=['8.8.8.8']
        self._client = MongoClient(URL)

    # save activity records
    def save_many(self, db, col, rec_set):
        # save array of records to database (db) and collection (col)
        db = self._client[db]
        col = db[col]
        ret = col.insert_many(rec_set)
        pprint(ret)
        
    def find(self, db, col, query):
        return self._client[db][col].find(query)
    
    def find_one(self, db, col, query):
        return self._client[db][col].find_one(query)
    
    # Main function used to access observtion data
    def aggregate(self, query):
        return self.aggregate2('test', 'Activity', query)
    
    def aggregate2(self, db, col, query):
        return self._client[db][col].aggregate(query)    
    
    def update(self, db, col, find, update):
        return self._client[db][col].update_many(find, update)
    
    def insert_one(self, db, col, doc):
        return self._client[db][col].insert_one(doc).inserted_id
    
    def update_one(self, db, col, match, update):
        return self._client[db][col].update_one(match, update, upsert=True)
    
    def get_last(self, db, col, query):
        # Get last record, designed for light
        #print(query)
        #self._client[db][col].find(query).sort({"time.timestamp": -1}).limit(1)
        curser =  self._client[db][col].find(query).limit(1)
        for doc in curser:
            return doc

    def delete_many(self, db, col, query):
        return self._client[db][col].delete_many(query)
    
def delete_many_test():
    print("Delete Many Test")
    query = {"subject.name":"Light"}
    mu = MongoUtil()
    doc = mu.delete_many(DB, OBSV_COL, query)
    pprint(doc)
    print("Done")

def insert_many_test():
    print("Insert Many Test")
    mu = MongoUtil()
    db = "foo"
    col = "bar"
    recs = []
    rec1 = {"foo":"foo"}
    rec2 = {"bar":"bar"}
    recs.append(rec1)
    recs.append(rec2)
    status = mu.save_many(db, col, recs)
    # None is a good result
    pprint(status)
    
def insert_one_test():
    print("Insert One Test")
    msg = {"Test":"One", "Time":datetime.now().timestamp()}
    mu = MongoUtil()
    id = mu.insert_one(DB, OBSV_COL, msg)
    print("Id", id)
    
def find_last_test():
    print("Find Last Test")
    #query = {"trial.id":'1', "subject.name":LIGHT, "subject.attribute.name":DURATION}
    query = {"trial.id":'1', "subject.name":LIGHT}
    mu = MongoUtil()
    doc = mu.get_last(DB, OBSV_COL, query)
    print(doc)
    print("Done")
    
if __name__=="__main__":
    #insert_many_test()
    #insert_one_test()
    #find_last_test()
    delete_many_test()
    print("Finished")
