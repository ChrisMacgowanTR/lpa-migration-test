#
# LPA Migration Test
# Data Object
# Chris Macgowan
# 14 Nov 2019
# data_object.py
#
# Since we need to collect key, value pairs that can have the same key value
# we will store a collection (list) of these data objects
# More news at 11pm
#
import logging

class DataObject:

    key = ''
    value = ''

    # method: DataObject()
    # brief: This would be the famous constructor
    # param: name - the name of the house you want
    # param: age - the age of the house you want
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def set(self, key, value):
        self.key = key
        self.value = value