#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:04:06 2019

@author: willy
"""

import os, re

# Renames files in the target folder matching regex to new name, 
#   by default replaces any opening dots for numbering purposes to dashes
def bulk_rename(folder_path, from_regex = "(?<=^[0-9])\.(?=[0-9]{1,2})", 
                to_regex = "-", recursive = False):       
    files = os.listdir(folder_path)
    if recursive:
        for f in files:
            if os.path.isdir(os.path.join(folder_path, f)):
                bulk_rename(os.path.join(folder_path, f), from_regex, to_regex, True)
                
    count = 0
    for f in files:
        new_name = re.sub(from_regex, to_regex, f)
        if new_name != f:
            new_path_name = os.path.join(folder_path, new_name)
            os.rename(os.path.join(folder_path, f), new_path_name)
            count += 1
    print("Files renamed in {}: {}".format(folder_path, count))
    
bulk_rename('/Users/willy/Dropbox/Books/', recursive = True)

