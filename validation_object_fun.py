#
# LPA Migration Test
# Validation Object Fun
# Chris Macgowan
# 05 Nov 2019
# validation_object_fun.py
#
# We will use this class to perform the id analysis.
# More news to follow
#
# Things might look like this >>>
#
# WE ARE THINKING
# We might have a class that will contain all this data for each table
# that we will define and then we will load them in the
# controller >>>

# The table dictionary
# clob_table_key       validation_object
# 'name'               name_object
# 'address'            address_object
#
# The Validation Object
#

import collections
import datetime
import logging
import json

import clob_parser as module_clob_parser

import validation_object as module_validation_object

import traceback
from pprint import pprint
from typing import OrderedDict


class ValidationObjectFun:

    # method: ValidationObjectFun()
    # brief: This would be the famous constructor
    # param: name - the name of the house you want
    # param: age - the age of the house you want
    def __init__(self):
        logging.debug('Inside: ValidationObjectFun::ValidationObjectFun()')

    # method: run()
    # brief: Validate the data in the row with the database
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run(self):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ValidationObjectFun::run()')
        logging.debug("Loading the data file")

        # Lets create a dictionary of objects

        # Creating a Dictionary
        # with Integer Keys

        compare_value_dictionary = {'LINE1' : 'line_1',
                                    'LINE2' : 'line_1',
                                    'STATE' : 'state_provedence'}

        # print(compare_value_dictionary)

        # create the object
        validation_object = module_validation_object.ValidationObject()
        validation_object.role_type = 'ADDRESS'
        validation_object.source_type = 'HELLO'
        validation_object.uuid = '98234769582347689523764'
        validation_object.role_data = 'this is an objetc'
        validation_object.clob_data = 'clob data'
        validation_object.values_dictionary = compare_value_dictionary

        # print(compare_value_dictionary)

        logging.debug('Inside: ValidationObjectFun::run()')
        logging.debug("Loading the data file")



