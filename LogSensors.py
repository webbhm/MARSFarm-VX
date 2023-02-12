'''
Handle getting sensor data and passing to outputs
'''


from STAT import STAT
from Save_Util import Saver
from MARSFarm_Util import *
from SI7021 import SI7021
from BME280 import BME280


class LogSensors(object):
    
    def __init__(self):
        # open database for duration
        self.save = Saver()
        self.stat = STAT()
        self.test = False
        
    def main(self):
        self.get_SI7021()
        self.get_BME280()
        
    def get_SI7021(self):
        # SI7021 Readings
        si = None
        try:
            si = SI7021()
        except Exception as e:
            # Low level failure (ie I2C or wiring)
            comment = "Failure getting SI7021"
            msg = self.stat.get_Env(TEMPERATURE, 0, CENTIGRADE, SI7021_, FAILURE,  comment)
            self.save_Env(msg)
            msg = self.stat.get_Env(HUMIDITY, 0, PERCENT, _SI7021_, FAILURE,  comment)
            self.save_Env(msg)
            return
            
        status, comment, temp = si.get_tempC()
        msg = self.stat.get_Env(TEMPERATURE, temp, CENTIGRADE, SI7021_, status, comment)
        self.save_Env(msg)
        
        status, comment, humidity = si.get_humidity()
        msg = self.stat.get_Env(HUMIDITY, humidity, PERCENT, SI7021_, status, comment)
        self.save_Env(msg)
        
    def get_BME280(self):
        # SI7021 Readings
        sensor = None
        try:
            sensor = BME280()
        except Exception as e:
            # Low level failure (ie I2C or wiring)
            comment = "Failure getting BME280"
            msg = self.stat.get_Env(TEMPERATURE, 0, CENTIGRADE, BME280_, FAILURE,  comment)
            self.save_Env(msg)
            msg = self.stat.get_Env(HUMIDITY, 0, PERCENT, BME280_, FAILURE,  comment)
            self.save_Env(msg)
            msg = self.stat.get_Env(PRESSURE, 0, HPA, BME280_, FAILURE,  comment)
            self.save_Env(msg)
            return
            
        status, comment, temp = sensor.getTemp()
        msg = self.stat.get_Env(TEMPERATURE, temp, CENTIGRADE, BME280_, status, comment)
        self.save_Env(msg)
        
        status, comment, humidity = sensor.getHumidity()
        msg = self.stat.get_Env(HUMIDITY, humidity, PERCENT, BME280_, status, comment)
        self.save_Env(msg)
        
        status, comment, value = sensor.getPressure()
        msg = self.stat.get_Env(PRESSURE, value, HPA, BME280_, status, comment)
        self.save_Env(msg)
        
    def save_Env(self, msg):
        if self.test:
            # Rewrite for testing
            msg[STATUS][STATUS_QUALIFIER] = TEST
        self.save.save_Obsv(msg)
        
def test():
    print("Test Log Sensors")
    ls = LogSensors()
    ls.test = True
    ls.main()
    print("Done")
    
def run():
    ls = LogSensors()
    ls.main()
        
if __name__=="__main__":
    #test()
    run()
    
