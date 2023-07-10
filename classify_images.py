#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Kolapo Adedipe
# DATE CREATED: July 10, 2023                    
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
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
import os
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
# Imports classifier function for using CNN to classify images
from classifier import classifier
from os.path import join
from os import listdir

def classify_images(images_dir, results_dic, model):
    """
    Classifies the pet images using a pretrained CNN model.
    Compares the classifications to the true identity of the pets and updates the results dictionary.

    Parameters:
    - image_dir: The directory path of the pet images.
    - results: The results dictionary to store the classification results.
    - model: The CNN model architecture to use for classification (e.g., 'resnet', 'alexnet', 'vgg').
    """

    # Iterate over the pet images
    for filename in results_dic:
        # Get the pet image label
        pet_label = results_dic[filename][0]
        
        # Create the file path for the image
        image_path = os.path.join(images_dir, filename)
        
        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model)
        
        # Format the classifier label
        classifier_label = classifier_label.lower().strip()
        
        # Add the classifier label to the results_dic
        results_dic[filename].append(classifier_label)
        
        # Compare the pet and classifier labels
        if pet_label in classifier_label:
            results_dic[filename].append(1)  # Match between labels
        else:
            results_dic[filename].append(0)  # No match between labels