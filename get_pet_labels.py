#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kolapo Adedipe
# DATE CREATED: July 05, 2023.                     
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    
    # Retrieve the filenames from the image directory
    filenames = listdir(image_dir)
    
    # Iterate through the filenames
    for filename in filenames:
        # Ignore hidden files
        if not filename.startswith('.'):
            # Remove file extension and convert to lowercase
            pet_label = filename.split('.')[0].lower()
            
            # Strip leading and trailing whitespace characters
            pet_label = pet_label.strip()
            
            # Add the label to the results dictionary
            results_dic[filename] = [pet_label]
    
    return results_dic