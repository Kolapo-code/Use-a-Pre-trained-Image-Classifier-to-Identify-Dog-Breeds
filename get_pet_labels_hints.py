#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels_hints.py
#                                                                             
# PROGRAMMER: Kolapo Adedipe
# DATE CREATED: July 05, 2023                                 
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function get_pet_labels that creates the pet labels from the image's
#          filename. This function inputs: 
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
    in_files = listdir(image_dir)
    results_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            pet_label = in_files[idx].lower().split('_')
            pet_label = ' '.join(pet_label[:-1])
            pet_label = pet_label.strip()

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])

    return results_dic