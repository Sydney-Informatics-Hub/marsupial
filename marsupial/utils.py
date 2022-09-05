import os
import re
import json
import pathlib
import subprocess
import torch
import pandas as pd
import numpy as np
from tqdm import tqdm
from pathlib import Path 
from PIL import Image
from datetime import datetime

"""
Image EXIF utilities

This set of functions is to extract information from image EXIF data. 

These functions are very useful when working with EXIF anotated images, like the NSWNP Wildcount dataset.
"""

def species_annotation_from_exif(image_file):
    # Get original species ID
    cmd="exiftool -Keywords " + '''"''' + str(image_file) + '''"'''
    image_keywords = subprocess.getoutput([cmd])
    species = re.findall(r'(?<=a\)\s).+?(?=\s\([a-zA-z])', image_keywords)
    return(species)

def date_time_original_from_exif(image_file):
    # Get DateTimeOriginal
    cmd="exiftool -DateTimeOriginal " + '''"''' + str(image_file) + '''"'''
    date_time_original = subprocess.getoutput([cmd])
    date_time_original = re.findall(r'(?<=:\s)(.*)', date_time_original)
    return(date_time_original)

def camera_name_from_exif(image_file):
    # Get Camera Name
    cmd="exiftool -UserLabel " + '''"''' + str(image_file) + '''"'''
    camera_name = subprocess.getoutput([cmd])
    camera_name = re.findall(r'(?<=:\s)(.*)', camera_name)
    return(camera_name)

def date_from_exif(image_file):
    # Get date
    cmd = "exiftool -DateTimeOriginal " + '''"''' + str(image_file) + '''"'''
    date = subprocess.getoutput([cmd])
    date = re.findall(r'(?<=:\s)([^\s]+)', date)
    return(date)

def time_from_exif(image_file):
    # Get time
    cmd = "exiftool -DateTimeOriginal " + '''"''' + str(image_file) + '''"'''
    time = subprocess.getoutput([cmd])
    time = time[time.rindex(' ')+1:]
    return(time)
