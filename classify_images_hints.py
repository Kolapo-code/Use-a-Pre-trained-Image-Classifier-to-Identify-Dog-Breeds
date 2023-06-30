#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py
#                                                                             
# PROGRAMMER: Kolapo Adedipe
# DATE CREATED: July 05, 2023                    
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 3" for the classify_images function 
#       Specifically EDIT and ADD code to define the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
import os
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        # Run classifier function to classify the images
        image_path = os.path.join(images_dir, key)
        model_label = classifier(image_path, model)
        
        # Process the model_label
        model_label = model_label.lower().strip()
        
        # Get the pet image label
        truth = results_dic[key][0]
        
        # Check if the pet image label is an exact match in the model label
        if truth in model_label:
            # Add the classifier label and match (1) to results_dic
            results_dic[key].extend([model_label, 1])
        else:
            # Add the classifier label and no match (0) to results_dic
            results_dic[key].extend([model_label, 0])