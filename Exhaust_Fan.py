'''
Basic control of the exhaust fan
Inherites from Fan_Class
Will get invoked from Thermostat
'''
from GPIO_Conf import EXHAUST_FAN
from Fan_Class import Fan_Class
from time import sleep
from datetime import datetime, time

class Exhaust_Fan(Fan_Class):
    
    def __init__(self):
        # set GPIO for exhaust
        self.gpio = EXHAUST_FAN
        super().__init__()

    def on(self):
        # override method so doesn't do anything so Rhonda can sleep at night without the fan noise
        print("Overridden and shut off so Rhonda can sleep without the noise")
        tm = datetime.now().time()
        if self.sleeping(tm) or self.napping(tm):
            return
            
        super().on()
        
    def napping(self, tm):
        if time(hour=13) < tm < time(hour=14, minute=30):
            print("Napping")
            return True
        else:
            return False
        
    def sleeping(self, tm):
        if time(hour=8) > datetime.now().time() < time(hour=22):
            print("Sleeping")
            return True
        else:
            return False
        
    
def test():
    print("Test Exhaust Fan")
    cf = Exhaust_Fan()
    print("Turn On")
    cf.on()
    sleep(5)
    print("Sleeping 23hr", cf.sleeping(time(hour=23)))
    print("Sleeping 2hr", cf.sleeping(time(hour=9)))
    print("Sleeping 10hr", cf.sleeping(time(hour=10)))

    print("Napping 2hr", cf.napping(time(hour=14)))
    print("Napping 9hr", cf.napping(time(hour=9)))
    print("Napping 10hr", cf.napping(time(hour=10)))
    print("Turn Off")
    cf.off()
    print("Done")

if __name__=="__main__":
    test()