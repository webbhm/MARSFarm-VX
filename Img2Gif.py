# The following libraries need to be installed:
# Author: Howard Webb
# Date: 2/12/2018
# This program selects pictures within a date range, then selects one per day and converts them to a GIF

import os
from datetime import datetime, timedelta
from PIL import Image

from location import location
from config import DB, IMAGE_COL
from MARSFarm_Util import FIELD, ID

PICTURE_DIR = '/home/pi/Pictures'
GIF_DIR = '/home/pi/Pictures/lapse'

def getPics(dir, type, start_date, end_date, hour, test=False):
    '''Select a picture of each day based on hour, since start of trial
           Args:
               dir: directory where pictures are located
               type: file format (usually jpg)
               start_date: start of the trial
               end_date: end time (usually current time)
               test:
           Returns:
               pics: array of file names
           Raises:
               None
    '''               
    if test:
        print("Get Pics from " + dir + " " + start_date + " to " + end_date)
        
    prior_day=0
    pics=[]
    for file in sorted(os.listdir(dir)):
        if file.endswith(type):
            # split by date separator
            dt=file.split('_')
            # split time from date
            tm=file.split('_')
            #print(file, tm)
            file_hour = tm[1][0:2]
            #if test:
                #print(file, dt, file_hour)

            # Set start date to earliest of 30 days or env value
            if dt[0] > start_date and dt[0] < end_date:
                # get one image per day
                day=dt[0].split('-')
                now=day[2]
                
#            print now, prior_day
                #print(int(hour) == int(file_hour))
                #if now!=prior_day:
                if int(hour) == int(file_hour) and now != prior_day: 
                    if test:
                        print(file + " " +  str(os.stat(dir + file).st_size))
                    prior_day = now
                    pics.append(dir+file)
    return pics

def pic_to_img(pics, test=False):
    '''Open pictures as images
           Args:
               pics: array of file names
               test:
           Returns:
               img: array of image structures
           Raises:
               None
    '''  
    if test:
        print("Open pictures as images")
    images=[]
    for p in pics:
        images.append(Image.open(p))
    return images        
        

def resize_images(images, size, test=False):
    '''Reduce image size for better processing and display
           Args:
               images: array if image data
               size: list of desired image size
               test:
           Returns:
               img: array of resized image structures
           Raises:
               None
    '''  

    if test:
        print("Resize: " + str(size))
    out = []
    for img in images:
        rimg = img.resize(size)
        out.append(rimg)
    return out

def get_start_date(test=False):
    '''Start date is the beginning of a trial - set in trial.py
        If env.py is missing, or data is invalid, then default to 4 weeks ago
           Args:
               None:
           Returns:
               start_date
           Raises:
               None
    '''  
    start_date = None
    tmp_date = str(datetime.now() - timedelta(days=30))
    print("Temp", tmp_date)
    try:
        from trial import trial
        start_date=trial["time"]["start_date_str"]
        print("Trial Start", start_date)
        if start_date < tmp_date:
            start_date = tmp_date
            print("Default", start_date)
    except Exception as e:
        if test:
            print(e)
        start_date  = tmp_date
        print("Error")
    if test:
        print("Start Date: " + start_date)
    return start_date

def make_gif(images, output_file, duration, test=False):
    '''Convert set of images to a GIF and saves to file
           Args:
               images: array of image data
               test:
           Returns:
               None:
           Raises:
               None
    '''  
    
    images[0].save(output_file, format='GIF', append_images=images[1:], save_all=True, duration=100, loop=0)
    if test:
        print("GIF Output: " + output_file)
        
def main(test=False):
    '''Main controller of processing
           Args:
               test:
           Returns:
               None:
           Raises:
               None
    '''  
    
    # Variables to control source and output
    start_date = get_start_date(test)
    end_date=str(datetime.now())
    hour = 11
    # Source of images
    # Image type to select
    type=".jpg"
    # Resize the image to 640x480 (resizing will keep ratio with one dimension specified)
    size=[640, 480]
    # gif location
    output_file = "/home/pi/python/static/plant.gif"
    # time to display image
    duration = 0.2
   
    # Output file name (will be in the python directory with this code)
    pics=getPics(PICTURES_DIR, type, start_date, end_date, hour, test)
    #print(len(pics))
    images = pic_to_img(pics, test)
    pics = resize_images(images, size, test)
    #print(len(pics))
    if len(pics) > 0:
        make_gif(pics, GIF_DIR, duration, test)
        move_gif(start_date, end_date, GIF_DIR)
    else:
        print("No pictures for criteria")
        
def move_gif(start_date, end_date, file):
    #move image to mongodb
    from pymongo import MongoClient
    from MongoUtil import MongoUtil
    import io
    
    # convert jpg to bytes
    im = Image.open(file)
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='GIF', save_all = True)
    
    # Build database structure
    # generate timestamp
    dt = datetime.now()
    ts = dt.timestamp() * 1000
    ts_str = format(dt, '%Y-%m-%d %H:%M:%S')
    name = format(dt, '%Y_%m_%d.gif')
    
    farm, field = get_farm()
    
    # One document per box holds both latest image and daily gif
    '''
    doc = {"location":location,
          "jpg":{'timestamp':ts,
           'time_str': ts_str,
           'name':<timestamp>.jpg
           'image': image_bytes.getvalue()},
          "gif": {'timestamp':ts,
           'start_date': start_date,
           'end_date': end_date,
           'farm':"MarsFarm_exp",
           'field':123,
           'name': <timestamp>.gif
           'image': image_bytes.getvalue()}
    }
    '''
    match = { "location.field.id":location[FIELD][ID]}
    update = { "$set":{"gif": {'timestamp':ts,
           'start_date': start_date,
           'end_date': end_date,
           'name':name,
           'image': image_bytes.getvalue()}
                       }}
    mg = MongoUtil()
    mg.update_one(DB, IMAGE_COL, match, update)
    print("Updated MongoDB", file)
    
def get_farm():
    # DEPRECATED
    #from trial import trial
    farm = location["farm"]
    field = location["field"]
    return farm, field
        
def test(test=False):
    '''Main controller of processing
           Args:
               test:
           Returns:
               None:
           Raises:
               None
    '''  
    
    # Variables to control source and output
    start_date = get_start_date(test)
    print("Start", start_date)
    end_date=str(datetime.now())
    print("End", end_date)
    hour = 11
    # Source of images
    dir="/home/pi/Pictures/"
    # Image type to select
    type=".jpg"
    # Resize the image to 640x480 (resizing will keep ratio with one dimension specified)
    size=[640, 480]
    # gif location
    output_file = "/home/pi/python/static/plant.gif"
    # time to display image
    duration = 0.2
   
    # Output file name (will be in the python directory with this code)
    pics=getPics(dir, type, start_date, end_date, hour, test)
    print("Count", len(pics))
    images = pic_to_img(pics, test)
    pics = resize_images(images, size, test)
    #print(len(pics))
    if len(pics) > 0:
        print("Make gif", output_file)
        make_gif(pics, output_file, duration, test)
        move_gif(start_date, end_date, output_file)
    else:
        print("No pictures for criteria")
    print("Done")        

def test2():
    test = True
    start_date = get_start_date(test)
    end_date=str(datetime.now())
    hour = 12
    # Source of images
    dir="/home/pi/Pictures/"
    # Image type to select
    type=".jpg"
    # Resize the image to 640x480 (resizing will keep ratio with one dimension specified)
    pics=getPics(dir, type, start_date, end_date, hour, test)


if __name__=="__main__":
    #main()
    test()
