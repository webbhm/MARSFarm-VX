'''
Controller function for the Lights
Author: Howard Webb
Date: 11/2/2022
'''
import Lights
from Recipe_Util import Recipe

t = Recipe()
# Get currrent light settings
fr, r, b, w = t.get_light_values()

# Create light and set to current values
lights = Lights.Light()
lights.customMode(fr, r, b, w)



