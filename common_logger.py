# -*- coding: utf-8 -*-

import os
import yaml
import logging
import logging.config

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