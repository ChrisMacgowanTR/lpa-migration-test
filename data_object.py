#
# LPA-ACORN Migration Test Tools
# Data Object
# Chris Macgowan
# 14 Nov 2019
# data_object.py
#
# The DataObject class will define a parent, key and value that can be used to
# represent a parsed object from the CLOB Parser.
#
# Since we need to collect key, value pairs that can have the same key value
# we will store a collection (list) of these data objects.
#
import logging

class DataObject:

    parent = ''
    key = ''
    value = ''

    # method: DataObject()
    # brief: This would be the famous constructor
    # param: parent - Name of the parent object parsed
    # param: key - Key of the parsed object
    # param: value - Value of the parsed object
    def __init__(self, parent, key, value):
        self.parent = parent
        self.key = key
        self.value = value

    def set(self, parent, key, value):
        self.parent = parent
        self.key = key
        self.value = value

    def get_parent(self):
        return self.parent

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value
