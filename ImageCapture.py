'''
Image Capture
1) Set camera lights
2) Take image
3) Save full image to Camer
4) Save small image to Camera/lapse
5) Reset lights

Author: Howard Webb
Date: 3/14/2021
3/16/2021 change to direct call of GrowLight
'''

#from Light_Check import CheckLight
from time import sleep
#from CameraAF import Camera
#from GrowLight import GrowLight
import os
from shutil import copy2
from config import DB, IMAGE_COL, PICTURE_COL
from Lights import Light


DIR_NAME = "/home/pi/Pictures"


def move_image():
    # move latest image to static directory for web showing
    files = sorted(filter(lambda x: os.path.isfile(os.path.join(DIR_NAME, x)), os.listdir(DIR_NAME)))
    file = files[-1]
    print("Move", file)
    #copy2(DIR_NAME+"/"+files[-1], DIr_NAME + /image.jpg" )
    
    #move image to mongodb
    from pymongo import MongoClient
    from PIL import Image
    from MongoUtil import MongoUtil
    import io
    from datetime import datetime
    from location import location
    from activity import activity
    
    print(location["farm"])
    print(location["field"])
    
    #database = "images"
    #collection = "latest"
    # convert jpg to bytes
    im = Image.open(DIR_NAME + '/' + file)
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')
    
    # ---------------------Extra for Flask website & Testing --------------------
    # Common data
    # generate timestamp
    dt = datetime.now()
    ts = dt.timestamp() * 1000
    ts_str = format(dt, '%Y-%m-%d %H:%M:%S')
    dtn = dt.timetuple()
    julian = (dtn.tm_year*1000) + dtn.tm_yday    
    
    # Get identifiers
#     farm, field = get_farm()
    mu = MongoUtil()
    
    # ------------- Flask Website specific  ---------------------
    
    # Build database structure for jpg & png
    # One document per box holds both latest image and daily gif
    doc = {"location":{
           'farm':location['farm'],
           'field':location['field']},
          "jpg":{'timestamp':ts,
           'time_str': ts_str,
           'image': image_bytes.getvalue()},
          "gif": {'timestamp':ts,
           'time_str': ts_str,
           'farm':location['farm'],
           'field':location['field'],
           'image': image_bytes.getvalue()}
    }

    match = { "location.field.id":location['field']['id']}
    update = { "$set":{"jpg":{'timestamp':ts,
                           'time_str': ts_str,
                           'name':file,   
                           'image': image_bytes.getvalue()}
                       }}

    mu.update_one(DB, IMAGE_COL, match, update)
    # save copy to new site
    #match = { "location":{"farm.id": farm_id, "field.id":field_id} }
    
    #mg.update_one('Production', 'image', match, update)
    print("Updated MongoDB")
    
    # --------------- Marsfarm_V2 specific Testing -------------------- 
    # One document per image
    doc = {"location":{
           'farm':location['farm'],
           'field':location['field']},
          "image":{'timestamp':ts,
           'time_str': ts_str,
           'Julian':julian,        
           'image': image_bytes.getvalue()},
    }
    
    mu.insert_one(DB, PICTURE_COL, doc)
    print("Image Added MongoDB")

  
def get_farm():
    from trial import trial
    farm = trial["location"]["farm"]
    field = trial["location"]["field"]
    return farm, field

def main():
    # Set lights, take picture, reset lights and move image

    print("Take Picture")
    # not object so runs on import
    import CameraAF
    print("Move")
    move_image()
    print("Done")
    
def test():
    print("Test get farm")
    farm, field = get_farm()
    print("Farm", farm, "Field", field)

# move image
if __name__ == "__main__":
    main()
    #test()