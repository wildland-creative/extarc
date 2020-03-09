# -*- coding: utf-8 -*-
"""functions for interacting / manipulating feature classes and tables - i.e.,
for manipulating objects, not attributes.
"""
import os

import arcpy
import logging

def get_unused_scratch_gdb_obj(fc_name = "next_fc"):
    """Given a name, will return the next empty feature class within the scratch
    geodatabase, appending an incrementing counter to the end until a non-existant
    feature class location is found.

    Args:
        fc_name (str): the desired name of the feature class

    Returns:
        scratch_path (str): the full path in the scratch geodatabase to the next
            non-existent fcnameX feature class.
    """

    return get_unused_obj_in_gdb(arcpy.env.scratchGDB, fc_name)

def get_unused_obj_in_gdb(gdb, fc_name = "next_fc"):
    """Given a name, will return the next empty feature class within the gdb,
    appending an incrementing counter to the end until a non-existant
    feature class location is found.

    Args:
        fc_name (str): the desired name of the feature class

    Returns:
        scratch_path (str): the full path in the geodatabase arg to the next
            non-existent fcnameX feature class.
    """

    logger = logging.getLogger(__name__)
    
    count = 0
    temp_fc = gdb + os.path.sep + fc_name

    while (arcpy.Exists(temp_fc)):
        temp_fc = gdb + os.path.sep + fc_name + str(count)
        count = count + 1

    logger.debug("Next empty fc is located at " + temp_fc)

    return temp_fc
    

def make_and_get_copy_in_scratch_gdb(fc, fc_name = "next_fc", projection = None):
    new_fc = get_unused_scratch_gdb_obj(fc_name)
    
    if projection is not None:
        arcpy.Project_management(fc, new_fc, projection)
    else:
        arcpy.CopyFeatures_management(fc, new_fc)
        
    return new_fc

def get_unused_fc_in_memory(fc_name = "next_fc"):
    """Given a name, will return the next empty in memory feature class,
    appending an incrementing counter to the end until a non-existant
    feature class location is found.

    Args:
        fc_name (str): the desired name of the feature class

    Returns:
        scratch_path (str): the full path in the geodatabase arg to the next
            non-existent fcnameX feature class.
    """
    return get_unused_obj_in_gdb("in_memory", fc_name)

def wipe_in_memory():
    # @TODO https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm
    #arcpy.Delete_management(out_data)

    return None

def wipe_scratch_gdb():
    # @TODO https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm
    #arcpy.Delete_management(out_data)
    return None


