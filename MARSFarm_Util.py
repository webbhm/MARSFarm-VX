'''
Constants used by MARSFarm apps for consistency 
'''

# Spreadhseet Columns
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
J = 10
K = 11
L = 12
M = 13
O = 15
U = 21
V = 22
# Spreadsheet Return status
DATA_SUCCESS = 0
DATA_INVALID = 2
DATA_MISSING = 1

ROW = "row"

ON = True
OFF = False

# Sensor Names
SI7021_ = "SI7021"
BME280_ = "BME280"
PUMP = "Pump"

# Data fields
#Location
LOCATION = "location"
FARM = "farm"
SCHOOL = "school"
FIELD = "field"
PLOT = "plot"

EXPERIMENT = "experiment"

TRIAL = "trial"

ID = "id"
DATE = "date"
TIME = "time"
TIMESTAMP = "timestamp"
TIME_STR = "timestamp_str"
END_DATE = "end_date"
DAY = "day"
WEEK = "week"

ACTIVITY_TYPE = "activity_type"
SUBJECT = "subject"
ATTRIBUTE = "attribute"
NAME = "name"
TYPE = "type"

PARTICIPANT='participant'
PARTICIPANT_TYPE='type'
PERSON='person'
SENSOR='sensor'

STATUS = "status"
STATUS_QUALIFIER = "status_qualifier"
STATUS_REASON = "status_reason"
SUCCESS = "Success"
FAILURE = "Failure"
UNKNOWN = "Unknown"
IN_PROCESS = "In_Process"
COMPLETE = "Complete"
TEST="Test"
COMMENT = "comment"

VALUE = "value"
UNIT = "unit"
COUNT = "count"
WEEK = "week"
SCORE = "score"
MISSING_DATA = "missing_data"
INVALID_DATA = "invalid_data"

START_DATE = "start_date"
END_DATE = "end_date"
START_DATE_STR = "start_date_str"
END_DATE_STR = "end_date_str"

ELEVATION = "elevation"
TYPE = "type"
GBE_ID = "GBE_Id"

PHENOTYPE_OBSERVATION = "Phenotype_Observation"
ENVIRONMENT_OBSERVATION = "Environment_Observation"
AGRONOMIC_ACTIVITY = "Agronomic_Activity"

#Subjects
PLANT = "Plant"
SEED = "Seed"
LEAVES = "Leaves"
ROOT = "Root"
TREATMENT = "Treatment"
AIR = "Air"
SOIL = "Soil"
LIGHT = "Light"

# Agronomic Activities
IRRIGATION = "Irrigation"
PLANTING = "Planting"
GERMINATION = "Germination"

# Attributes
AMBIENT_TEMP = "ambient_temp"
TEMP = "Temperature"
TEMPERATURE = TEMP
PRESSURE = "Pressure"
LENGTH = "Length"
HEIGHT = "Height"
WIDTH = "Width"
DEPTH = "Depth"
HUMIDITY = "Humidity"
VOLUME = "Volume"
HEALTH = "Health"
FRESH_MASS = "fresh_mass"
DENSITY = "Density"
EDIBLE_MASS = "Edible_mass"
INEDIBLE_MASS = "Inedible_mass"
CO2 = "CO2"
DURATION = "Duration"
SPECTRUM = "Spectrum"

# Units
PERCENT = "%"
CENTIGRADE = "C"
#CENTIMETER = "cm"
MILIMETER = "mm"
#CUBIC_CENTIMETER = "cm2"
CUBIC_MILIMETER = "mm2"
SCALE = "scale"
GRAM = "gram"
G_CUBIC_CENTIMETER = "g/cm2"
MILILITER = "ml"
HPA="hpa"
MINUTES = "minutes"
PWM = "pwm"

# Charting parameters
X_COL = "x_column"
Y_COL = "y_column"
Z_COL = "z_column"
ERROR = "error"
ERROR_MINUS = "error_minus"
ERROR_PLUS = "error_plus"
TEMPLATE = "template"
ERROR_MSG = ""
COLOR = "color"
TITLE = "title"
HOVER_DATA = "hover_data"
VAL = "val"
MAX = "max"
MIN = "min"

TWO = "2"
THREE = "3"
FOUR = "4"
WEEK = "week"

SCHOOLS = ['Academir Charter School West', 'Air Base K-8 Center for International Education', 'Archbishop Coleman Carroll High School', 'Archimedean Upper Conservatory', 'Barbara Goleman SH', 'Carrollton School of the Sacred Heart', 'Christi/STEPSS Academy ', 'Coconut Palm K8 Academy', 'Congress Middle School', 'Coral Reef senior', 'Country Club Middle School', 'Cutler Bay Middle', 'Dorothy M. Wallace COPE Center HS', 'Dorothy M. Wallace COPE Center MS', 'Dr Michael Krop SHS', 'Everglades high school', 'Felix Varela SHS', 'Florida Christian School HS', 'Florida Christian School MS', 'G. Holmes Braddock Senior High', 'Glades Middle Miami Dade', 'Gulliver Charlinne Garcia', 'Gulliver MS Brian Reynoso', 'Gulliver MS Sam Fezza', 'Gulliver Prep School', 'Palmer Trinity School (MS)', 'Palmetto Middle School (MS)', 'Redland Middle School', 'Richmond Heights Middle School', 'Riviera Middle ', 'Robert Morgan Educational Center', 'Robert Renick Educational Center', 'Rockway MS', 'Ruben Dario Middle', 'Ruth Owens Kruse', 'SSEDS  school 2 (N)', 'Santaluces High School', 'Scheck Hillel Community School (HS)', 'Somerset Academy Charter High ', 'South Dade Middle School', 'South Dade Senior High School', 'South Miami Middle School', 'South Miami SHS', 'SouthTech Academy', 'Sseds School 1 (AIC)', 'St Kevin Catholic School', 'TERRA Environmental Institut', 'The Conservatory School of North Palm Beach', 'Vineland K8 Center', 'Watson B. Duncan Middle School', 'West Miami Middle ']
ATTRIBUTES = [HEIGHT, WIDTH, DEPTH, EDIBLE_MASS]