import sys
import os
from os import path
from PIL import Image

#grab first and second argument

source_folder = sys.argv[1]
target_folder = sys.argv[2]
#check if new exists, else create a new one

print(source_folder)
print(target_folder)
png_loc = "C:\Python\Python-OOPS\Image_Processing\pngs"
pokedex_loc = "C:\Python\Python-OOPS\Image_Processing\Pokedex"
is_dir = os.path.isdir(png_loc) 
print(is_dir)
if not is_dir:
        
    # Parent Directory path  
    parent_dir = "C:\Python\Python-OOPS\Image_Processing"
        
    # Path  
    path = os.path.join(parent_dir, target_folder)  
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
        
print("The location of the folder is " + png_loc)    
#loop through Pokedex
for filename in os.listdir(pokedex_loc):
    if filename.endswith(".jpg"):
        im = Image.open(pokedex_loc+'\\'+filename)
        file = os.path.splitext(filename)[0]
        print(file)
        im.save(png_loc+'\\' + file +'.png')
    else:
        continue

#convert images to png
for filename in os.listdir(png_loc):
    if filename.endswith(".png"):
        print(filename)
    else:
        continue