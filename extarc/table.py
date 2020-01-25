# -*- coding: utf-8 -*-
"""functions for use with the attribute table
"""

import pandas as pd
import arcpy

def get_arcgis_table_as_df(in_fc, input_fields=None, query=""):
    """Function will convert an arcgis table into a pandas dataframe with an
    object ID index, and the selected input fields using an
    arcpy.da.SearchCursor."""
    
    OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
    
    if input_fields:
        final_fields = [OIDFieldName] + input_fields
    else:
        final_fields = [field.name for field in arcpy.ListFields(in_fc)]
        
    data = [row for row in arcpy.da.SearchCursor(
            in_fc, final_fields, where_clause=query)]
    
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
        
    return fc_dataframe


def get_oid_fieldname(fclass):
    """This retrieves the OID field name from a feature class if it exists.
        Otherwise, None is returned.

    Args:
        fclass (string): A string with the location of the feature class to
        retrieve OID for

    Returns:
        a string containing the OID field name or None
    """
    desc = arcpy.Describe(fclass)
    
    if (desc.hasOID == True):
        return desc.OIDFieldName
    
    return None

def translate_ftype_for_addition(ftype):
    """Arcpy is stupid and isn't consistent with their type names between 
        describing a field and adding it. This will map them correctly.
        
    Args:
        ftype (string): the type as returned from type attribute of a Field
        object - other arguments will not result in a logical result

    Returns:
        a string containing the field type for use in new field creation
    """
    if (ftype == "Integer"):
        return "LONG"
    elif (ftype == "String"):
        return "TEXT"
    elif (ftype == "SmallInteger"):
        return "SHORT"
    elif (ftype == "OID"): # OID is a long but its it's own type
        return "LONG"
    else:
        return ftype

def copy_to_new_field(fc, fname, newfname):
    """Adds a new field to the feature class named 'newfname' of same
        type as 'fname' and copies the contents.
        
    Args:
        fc (string): The feature class that's being modified
        fname (string): The field to be copied
        newfname (string): The new field
    """
    
    old_field = arcpy.ListFields(fc, fname)[0]
    
    new_type = translate_ftype_for_addition(old_field.type)
    
    arcpy.AddField_management(fc, newfname, new_type)
    
    rows = arcpy.UpdateCursor(fc)
    
    for row in rows:
        fvalue = row.getValue(fname)
        row.setValue(newfname, fvalue)
        rows.updateRow(row)
    del row, rows

def get_unique_field_values(fc, field_name) :
    """
    Iterates over a feature class and gets all the unique values contained in
    field_name.
    
    Args:
        fc (string): The feature class of consideration
        field_name (string): the field to get unique values from
        
    Returns:
        the unique values of field_name

    """
    with arcpy.da.SearchCursor(fc, [field_name]) as cursor:
        return sorted({row[0] for row in cursor})
