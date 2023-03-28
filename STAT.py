'''
Create database message structures
Author: Howard Webb
Date: 2023-002011
'''
from activity import activity
from location import location
from MARSFarm_Util import *
from Time_Util import get_time_struct
from datetime import datetime


class STAT(object):
    
    def __init__(self):
        
        self.experiment = activity[EXPERIMENT]
        self.trial = activity[TRIAL]

        self.trial_start_date = activity[TIME][TIMESTAMP]
        self.trial_active = True
        if STATUS in activity.keys() and activity[STATUS] == COMPLETE:
            self.trial_active = False
            self.trial_start_date = None
            
    def get_Env(self, attribute, value, unit, participant, status_qualifier, comment):
        actvty = ENVIRONMENT_OBSERVATION
        return self.get_Activity(actvty, AIR, attribute, value, unit, participant, status_qualifier, comment)
        
    def get_Agro(self, attribute, value, unit, participant, status_qualifier, comment):
        actvty = AGRONOMIC_ACTIVITY
        return self.get_Activity(actvty, TREATMENT, attribute, value, unit, participant, status_qualifier, comment)

    def get_Activity(self, actvty, subject, attribute, value, unit, participant, status_qualifier, comment):
        #Generic activity
        attribute = {NAME:attribute, VALUE:value, UNIT:unit}
        subject = {NAME:subject, ATTRIBUTE:attribute}
        if comment is None:
            status = {STATUS_QUALIFIER:status_qualifier}
        else:
            status = {STATUS_QUALIFIER:status_qualifier, COMMENT:comment}
        participant = {NAME:participant, PARTICIPANT_TYPE:SENSOR}
        time = get_time_struct(self.trial_start_date)
        if self.trial_active:
            # if during trial, add trial and experiment
            msg = {TIME:time, TRIAL:self.trial, EXPERIMENT:self.experiment, LOCATION:location, ACTIVITY_TYPE:actvty, SUBJECT:subject, PARTICIPANT:participant, STATUS:status}
        else:
            msg = {TIME:time, LOCATION:location, ACTIVITY_TYPE:actvty, SUBJECT:subject, PARTICIPANT:participant, STATUS:status}
        return msg
    
    def get_spectrum(self, spec):
        # Spectrum record, create when turn lights on
        attribute = {NAME:SPECTRUM, VALUE:spec, UNIT:PWM}
        subject = {NAME:LIGHT, ATTRIBUTE:attribute}
        status = {STATUS_QUALIFIER:SUCCESS}
        participant = {NAME:LIGHT, PARTICIPANT_TYPE:SENSOR}
        time = get_time_struct(self.trial_start_date)
        msg = {}
        if self.trial_active:
            msg = {TIME:time, TRIAL:self.trial, EXPERIMENT:self.experiment, LOCATION:location, ACTIVITY_TYPE:ENVIRONMENT_OBSERVATION, SUBJECT:subject, PARTICIPANT:participant, STATUS:status}
        else:
            msg = {TIME:time, LOCATION:location, ACTIVITY_TYPE:ENVIRONMENT_OBSERVATION, SUBJECT:subject, PARTICIPANT:participant, STATUS:status}
        return msg
        
    def get_light_on(self, spec):
        # Returns two records when lights turned on:
        # Light on record, long time period event, has start and end dataes
        # Creates spectrum record (both same timestamp)
        attribute = {NAME:DURATION, VALUE:0, UNIT:MINUTES}
        subject = {NAME:LIGHT, ATTRIBUTE:attribute}
        status = {STATUS:IN_PROCESS, STATUS_QUALIFIER:UNKNOWN}
        participant = {NAME:LIGHT, PARTICIPANT_TYPE:SENSOR}
        time = get_time_struct(self.trial_start_date)
        msg = {}
        if self.trial_active:
            msg = {TIME:time, TRIAL:self.trial, EXPERIMENT:self.experiment, LOCATION:location, ACTIVITY_TYPE:ENVIRONMENT_OBSERVATION, SUBJECT:subject, PARTICIPANT:participant, STATUS:status}
        else:
            msg = {TIME:time, LOCATION:location, ACTIVITY_TYPE:ENVIRONMENT_OBSERVATION, SUBJECT:subject, PARTICIPANT:participant, STATUS:status}

        msg2 = self.get_spectrum(spec)
        return msg, msg2
        
    def get_light_off(self, duration):
        # Create update portion only
        time = datetime.now().timestamp()
        msg = {'$set':{'subject.attribute.value':duration, 'status.status':COMPLETE, 'status.status_qualifier':SUCCESS}}
        return msg
        

def test():
    print("Test Observation Utility")
    spec = {"FarRed":56, "Red":75, "Blue":44, "Green":95}
    s = STAT()
    
    msg = s.get_Env(TEMPERATURE, 23.5, CENTIGRADE, SI7021_, SUCCESS, None)
    print(msg)
    print("Spectrum")
    msg = s.get_spectrum(spec)
    print(msg)
    print("Test Light On")
    msg = s.get_light_on(spec)
    print(msg)
    print("Test Light On")
    msg = s.get_light_off(120)
    print(msg)
    print("Done")
    
if __name__=="__main__":
    test()    
               