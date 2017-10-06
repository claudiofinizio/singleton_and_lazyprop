#! /usr/bin/python
# -*- coding: utf-8 -*-
# Python standard libraries
import logging
from logging.handlers import (
    RotatingFileHandler,
    TimedRotatingFileHandler,
)
import os

# Python 3rd-part libraries

# Project modules

# Modules only for debugging
from pprint import pprint

# Define logs' files directories.
logs_directory = "logs"
logs_dirname = os.path.join(
    os.path.dirname(__file__),
    logs_directory,
)
logs_extension = "log"

# Customize the basic logger.
basic_fileroot = "basic_logs"
logging.basicConfig(
    level="DEBUG",
    format='[%(asctime)-10s] [%(levelname)8s] %(name)s: %(message)s',
    datefmt="%Y-%m-%d@%H:%M:%S",
    filename=os.path.join(
        logs_dirname, ".".join([basic_fileroot, logs_extension])
    ),
    filemode="w"
)

# Create handlers.
# Non-rotating handlers
dev_handler = logging.FileHandler(
    filename="logs/dev_log.log",
    mode="w",
    encoding="UTF-8",
)
dist_handler = logging.FileHandler(
    filename="logs/dist_log.log",
    mode="w",
    encoding="UTF-8",
)

"""
# Rotating handlers
dev_fileroot = "dev_log"
dev_handler = RotatingFileHandler(
    filename=os.path.join(
        logs_dirname, ".".join([dev_fileroot, logs_extension])
    ),
    encoding="UTF-8",
    maxBytes=2000,
    backupCount=15,
)
dist_fileroot = "dist_log"
dist_handler = TimedRotatingFileHandler(
    filename=os.path.join(
        logs_directory, ".".join([dist_fileroot, logs_extension])
    ),
    encoding="UTF-8",
    when="S",
    interval=1,
    backupCount=50,
)
"""

dev_formatter = logging.Formatter(
    fmt="%(name)20s %(message)s",
    datefmt="%Y-%m-%d@%H:%M:%S",
)
dev_handler.setFormatter(dev_formatter)
dist_formatter = logging.Formatter(
    fmt="[%(asctime)10s] %(levelname)-8s %(name)-15s %(message)s",
)
dist_handler.setFormatter(dist_formatter)


def dev_logger_factory(logger_name, level=logging.DEBUG):
    dev_logger = logging.getLogger(logger_name)
    dev_logger.setLevel(level)
    dev_logger.addHandler(dev_handler)
    return dev_logger




def dist_logger_factory(logger_name, level=logging.INFO):
    dist_logger = logging.getLogger(logger_name)
    dist_logger.setLevel(level)
    dist_logger.addHandler(dist_handler)
    return dist_logger