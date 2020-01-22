# -*- coding: utf-8 -*-
"""functions for controlling messages to arcpy and logging
"""

import os
import yaml
import logging
import logging.config
import arcpy

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
        
def send(msg, severity=0):
    logger = logging.getLogger(__name__)
    
    # outputs message using python logging module, choosing type
    # based on severity
    if severity == -1:
        logger.debug(msg)
    elif severity == 0:
        logger.info(msg)
    elif severity == 1:
        logger.warning(msg)
    elif severity == 2:
        logger.error(msg)
    
    try:
        for string in msg.split('\n'):
            # debug messages are never output to arcpy by default
            if severity == 0:
                arcpy.AddMessage(string)
            elif severity == 1:
                arcpy.AddWarning(string)
            elif severity == 2:
                arcpy.AddError(string)
    except:
        pass
