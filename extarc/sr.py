# -*- coding: utf-8 -*-

import arcpy

def get_sr_by_fc(fc):
    """This retrieves a spatial reference object by its factory code. Per a
        relevant gis stack exchange,
        
        > If an Esri well-known ID is below 32767, it corresponds to the EPSG
        > ID. WKIDs that are 32767 or above are Esri-defined. Either the object
        > isn't in the EPSG Geodetic Parameter Dataset yet, or it probably
        > won't be added. If an object is later added to the EPSG Dataset, Esri
        > will update the WKID to match the EPSG one, but the previous value
        > will still work.
        
        It should therefore be sufficient to pass the EPSG without worry.

    Args:
        fc (int): An integer representing the spatial reference's factory code.

    Returns:
        an arcpy SpatialReference object for corresponding factory code.
    """
    sr = arcpy.SpatialReference(fc)
    return sr


def get_sr_nad83_gcs():
    """Returns the spatial reference for NAD83 GCS (unprojected).

    Returns:
        an arcpy SpatialReference object for NAD83 GCS (unprojected).
    """
    sr = get_sr_by_fc(4269)
    return sr

def get_sr_nad83_rispf():
    """Returns the spatial reference for NAD83 Rhode Island State Plane Feet.

    Returns:
        an arcpy SpatialReference object for NAD83 Rhode Island State Plane Feet.
    """
    sr = get_sr_by_fc(3438)
    return sr

def get_sr_nad83_utm_z19():
    """Returns the spatial reference for NAD83 UTM Zone 19.

    Returns:
        an arcpy SpatialReference object for NAD83 UTM Zone 19.
    """
    sr = get_sr_by_fc(26919)
    return sr

def get_sr_wgs84():
    """Returns the spatial reference for WGS84 (unprojected).

    Returns:
        an arcpy SpatialReference object for WGS84.
    """
    sr = get_sr_by_fc(4326)
    return sr