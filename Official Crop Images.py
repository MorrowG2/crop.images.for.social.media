#!/usr/bin/python                                                  
from PIL import Image                                              
import os, sys                       

# Enter your path below in the 'path' variable
path = r"C:\Users\"
dirs = os.listdir(path)
Image.MAX_IMAGE_PIXELS = None

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            # Get rid of RGBA or RGB for PDF saves
            # RGBA is alpha
            im = im.convert("RGB")
            #RGBA is for PNG only while RGB is for JPG
            # 4500, 5400 Merch by Amazon
            #600, 900 for Pinterest
            imResize = im.resize((600,418), Image.ANTIALIAS)

        # CHANGE TO PNG or whatever you want to save the file as
            imResize.save(f+'.pdf', quality=95)

resize()
# It created double images when I selected JPG
