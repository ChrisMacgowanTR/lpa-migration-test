#
# LPA Migration Test
# Main Application
# Chris Macgowan
# 05 Nov 2019
# app.py
#
# We will use this to search for the id in a number of database mapping tables. Maybe one
# day we can use this to build aip profile.
#
# Usage:
# - Provide a ID as a variable and run the analysis
# - Provide a file with some IDs and run the analysis on the entire file
#

import logging
import sys
import traceback
# import psycopg2

import parse_dictionary as module_parse_dictionary
#import idmap_analysis_wca_guid as module_idmap_analysis_wca_guid

file_handler = logging.FileHandler(filename='idmap_utility.log')
stdout_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    handlers=handlers
)

logging.info('LPA Migration Test')
logging.info('The application is starting')
logging.debug("Starting postgresql-connect")
logging.debug("Set input source")

parse_dictionary = module_parse_dictionary.ParseDictionary()

# This is a test of pandas and loading data into the the container from SQL
# database connection. We was testing this out for Lori
parse_dictionary.run3()

logging.info('The end if near!')
logging.info('LPA Migration Test')
logging.info('The application is stopping')
logging.info('Have a nice day')
