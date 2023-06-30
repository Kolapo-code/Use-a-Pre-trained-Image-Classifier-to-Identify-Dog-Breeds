#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args_hints.py
#                                                                             
# PROGRAMMER: Kolapo Adedipe
# DATE CREATED: July 05, 2023                                  
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function that retrieves the following 3 command line inputs from
#          the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', type=str, default='pet_images/', help='path to folder of images')
    parser.add_argument('--arch', type=str, default='vgg', help='the CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file of names of dog breeds')

    args = parser.parse_args()
    return args