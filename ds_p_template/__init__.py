"""Datashark LVM Plugin
"""
from .__version__ import version, version_tuple
from ds_core.logging import LOGGING_MANAGER

NAME = 'template'
LOGGER = LOGGING_MANAGER.get_logger(NAME)