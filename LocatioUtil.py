'''
Helper for location information
'''
from location import location
from FileUtil import saveDict
from MARSFarm_Util import *

class Location_Util(object):
    
    def __init__(self):
        self._location = {FARM:{}, FIELD:{}}
        # field id is the hardware id
        self._location[FIELD][ID] = getserial()
        
    def save(self):
        saveDict('location', 'python/Location.py', self._location)
        
    def set_farm_name(self, name):
        self._location[FARM][NAME] = name

    def set_farm_id(self, id):
        self._location[FARM][ID] = id

    def set_field_name(self, name):
        self._location[FIELD][NAME] = name


def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial

def test():
    print("Test Location Util")
    l = Location_Util()
    l.set_farm_name('MARSFarm_1')
    l.set_farm_id('MARSFarm_1')
    l.set_field_name('MARSFarm_F1')
    print(l._location)
    print("Done")

if __name__=='__main__':
    test()