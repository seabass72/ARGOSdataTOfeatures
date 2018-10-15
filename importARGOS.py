##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2018
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

#import packages

import sys,os, arcpy

# Set input variables (Hard-wired)

inputFile = 'V:/ARGOSTracking/Data/ARGOSData/1997dg.txt'
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

# open the ARGOS data file for reading

inputFileObj = open(inputFile, 'r')

# while loop: get the first of the line

lineString = inputFileObj.readline()

while lineString:
                                # set code to only run if line contains date 
    if "Date :" in lineString:

# split the line string into list
        lineList = lineString.split()

# save the attributes from the first line 
        tagID = lineList[0]

# get the next line

        line2String = inputFileObj.readline()
        line2Data = line2String.split()
        print(line2Data)
        
       
    # get attributes from next line
        obsLat = line2Data[2]
        obsLon = line2Data[5]
        print(tagID,obsLat,obsLon)
       

        


    #get next line
    lineString = inputFileObj.readline()
