'''
class representation of the pump
Author: Howard Webb
Date 11/2/2022

NOTE: The pump was designed to be reversable, but not implemented
needs more development to implement
'''

from pigpio import pi, OUTPUT
from time import sleep
from GPIO_Conf import PUMP_POS, PUMP_GND, ON, OFF
from STAT import STAT
from Save_Util import Saver
from MARSFarm_Util import *

pi = pi()


class Pump:
    def __init__(self, gpio_pinA=None, gpio_pinB=None):
        self.gpioA = PUMP_POS #Store pump GPIO
        self.gpioB = PUMP_GND #Store pump GPIO
        self.calibration = 0.7 ; #Rate of pumping, measured in ml/sec 
        pi.set_mode(self.gpioA, OUTPUT) #Set pump as output
        pi.set_mode(self.gpioB, OUTPUT) #Set pump as output
        pi.write(self.gpioA,OFF) #Turn off pump when initialized
        pi.write(self.gpioB,OFF) #Turn off pump when initialized
        
        self._test = False
        

    def on(self):
        pi.write(self.gpioA,OFF) #set pump to state
        pi.write(self.gpioB,ON) #set pump to state

    def off(self):
        pi.write(self.gpioA,OFF) #set pump to state
        pi.write(self.gpioB,OFF) #set pump to state
        
    #Dispense 10mL of water
    def calibrate(self):
        self.setState(ON)#Begin pumping
        sleep(10*0.54);#Dispense 10mL
        self.setState(OFF) #End pumping
        
    #Dispense some user defined amount of water
    def dispense(self, volume):
        if (volume > 0):
            print("ON")
            self.on()#Begin pumping
            sleep(volume*self.calibration);#Pump volume number of mL
            self.off() #End pumping
            print("OFF")
            self.log(volume)
            
    def log(self, volume):
        st = STAT()
        s = Saver()
        status = SUCCESS
        if self._test:
            status = TEST
        msg = st.get_Agro(IRRIGATION, volume, MILILITER, PUMP, status, None)
        s.save_Obsv(msg)
        

def test():
    #gpio pin 24 is "forward" on the pump and gpio pin 23 intended to be "reverse" is not being used
    print("Test Pump")
    print('Pumping 10 ML as test')
    pump = Pump()
    pump._test = True
    pump.dispense(10)
    print("Done")

if __name__ == "__main__":
   test()
