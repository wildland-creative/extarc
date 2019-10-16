# -*- coding: utf-8 -*-
#
# this script sets up paths based on directory structure, eliminates
# some of the path maintenance in the scripts themselves

from os import path
import os
import sys

# get the arcmap directories, taken from
# https://my.usgs.gov/confluence/display/EGIS/Using+Anaconda+modules+from+the+ESRI+python+environment
arcmap_path = os.environ["AGSDESKTOPJAVA"]
pp = arcmap_path.find("Desktop")
arcver = arcmap_path[pp+7:pp+11] # "10.4"
arcmap_exe = os.path.join(arcmap_path, "bin", "ArcMap.exe")

# set arcpy directories to add the arcpy module
ARC32_BIN = path.join(arcmap_path, 'bin')
ARC32_PY = path.join(arcmap_path, 'ArcPy')
ARC32_SCRIPTS = path.join(arcmap_path, 'ArcToolBox', 'Scripts')

def append_arc32_paths():
    """Appends the ArcDesktop directories in order to import the arcpy module.
    """
    sys.path.append(ARC32_PY)
    sys.path.append(ARC32_BIN)
    sys.path.append(ARC32_SCRIPTS)