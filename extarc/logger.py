# -*- coding: utf-8 -*-
"""functions for controlling messages to arcpy and logging
"""

import os
import yaml
import logging
import logging.config
import logging.handlers

import arcpy

class ArcPyLogHandler(logging.StreamHandler):
    """
    Custom logging class that bounces messages to the arcpy tool window as well
    as reflecting back to the file.
    """

    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        """
        Write the log message
        """
        if record.levelno >= logging.ERROR:
            arcpy.AddError(record.msg)
        elif record.levelno >= logging.WARNING:
            arcpy.AddWarning(record.msg)
        elif record.levelno >= logging.INFO:
            arcpy.AddMessage(record.msg)

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration
    
    Parameters
    ----------
    default_path : type
        Defaults to ``logging.yaml``, this is the path to the config file.
    default_level : type
        Defaults to ``logging.INFO``, this is the log level which you'd like
        to record.
    env_key : type
        Description of parameter `y` (with type not specified)
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
