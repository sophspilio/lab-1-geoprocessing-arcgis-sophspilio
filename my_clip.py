# Name: Sophie Spiliotopoulos
# Python Version: Python 2.7
# Description: Code Lab 1- a script to clip the lakes.shp based on the basin.shp file, to create a new layer that shows the lakes within the basin. 

import arcpy

#set environmnet
arcpy.env.workspace = "E:\\Comp Programming for GIS\\Data_Lab_1_Geoprocessing_ArcGIS"

#set local variables
lakes = "lakes.shp"
basin = "basin.shp"
lakes_myClip_shp = "E:\\Comp Programming for GIS\\Data_Lab_1_Geoprocessing_ArcGIS\\Results\\lakes_myClip.shp"

#process clip 
arcpy.Clip_analysis(lakes , basin ,lakes_myClip_shp, "")
