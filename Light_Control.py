'''
Controller function for the Lights
Author: Howard Webb
Date: 11/2/2022
'''
import Lights
from Trial_Util import Trial

t = Trial()
# Get currrent light settings
fr, r, b, w = t.get_light_values()

# Create light and set to current values
lights = Lights.Light()
lights.customMode(fr, r, b, w)



