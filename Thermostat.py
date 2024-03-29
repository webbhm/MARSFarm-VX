from Heater import Heater
from Exhaust_Fan import Exhaust_Fan
from Circulation_Fan import Circulation_Fan
#from SHTC3 import *
from SI7021 import SI7021
from Recipe_Util import Recipe
from GPIO_Conf import ON, OFF
import time
from datetime import datetime

class Thermostat(object):
    
    def __init__(self):
        self.tu = Recipe()
        self.efan = Exhaust_Fan()
        self.cfan = Circulation_Fan()
        self.heater = Heater()
        self.temp = SI7021()
        
    def get_temp(self):
        temperature = self.temp.get_tempC()
        return temperature
    
    def get_Setpoint(self):
        s = self.tu.get_setpoint()
        c = (s -32)*5/9 # convert fahrenheit to centigrade
        return c 
        
    def adjust(self):
        # Control code
        setpoint = self.get_Setpoint()
        status, comment, temp = self.get_temp()
        if temp is None:    
            print("Failure getting temp, no adjustment")
            return
        print("Set", setpoint, "Temp", temp)
        if ( temp < setpoint): #Measured temp is below setpoint
            self.heater.on() #Turn on heater to raise temp   
            self.cfan.on() # Set circ fan state
            print("Heater: On, Circ_Fan: ON")

        if ( temp >= setpoint): #Measured temp is above setpoint
            self.heater.off() #Turn off heater to lower temp
            print("Heater: OFF")

        # Exhaust fan control code
        if ( temp >= setpoint + 1): #Measured temp is above setpoint by too much
            self.efan.on() #Turn on exhaust fan
            print("Exhaust Fan: ON")
        else:
            self.efan.off() #Turn off fan
            print("Exhaust Fan: OFF")



def test():
    print("Thermostat Test")
    t = Thermostat()
    print("Adjust")
    t.adjust()
    print(datetime.now().isoformat())
    print("Done")
    
if __name__=='__main__':
    test()
  
