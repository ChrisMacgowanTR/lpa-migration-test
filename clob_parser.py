#
# LPA Migration Test
# CLOB Parser Utility
# Chris Macgowan
# 14 Nov 2019
# clob_parser.py
#
# We will use this class to parse the clob data.
#

import collections
import logging
import json

import data_object as module_data_object

class CLOBParser:

    resultList = []

    # method: CLOBParser()
    # brief: This would be the famous constructor
    # param: name - the name of the house you want
    # param: age - the age of the house you want
    def __init__(self):
        logging.debug('Inside: CLOBParser::CLOBParser()')

    # method: parse()
    # brief: Parse the given CLOB object for objects based on the search parent and
    # search keyword. A list of objects will be returned based on the search_parent
    # and search_keyword. If search_keyword is left empty a collection of objects will
    # be returned based on the search_parent. If the search_keyword is set the list
    # will return one object - based on the search_parent and search_keyword.
    #
    # param: clob - CLOB object to parse
    # param: search_parent - Parent of object to return
    # param: search_key - object key to parse. Empty will all objects
    # return: List of objects
    def parse(self,
              clob,
              search_parent,
              search_key):

        logging.debug('Inside: CLOBParser::parse()')

        active_key = ''

        print(json.dumps(clob, indent=2))

        # Note - we might want to use recussion to iterationt his stuff
        # We are fun playing here

        logging.debug("Start parsing ... ")

        for key in clob:
            logging.debug("index: %s", key)

            parent_key = key

            value = clob[key]

            # test the value of the object
            # if the value is a collections.OrderedDict we will
            # iterate on the object again - this is where the recussion can come in

            logging.debug("Determine the object type")
            logging.debug("Object type: %s", type(value))
            logging.debug("Data value: %s", value)

            if isinstance(value, (collections.OrderedDict)):
                # The object is a collection we will continuie
                # to iterate

                self.get_dictionary_object(value, active_key, parent_key, search_parent, search_key)
            else:
                logging.debug("Object type: %s", type(value))

        logging.debug("Done")
        return self.resultList

    # method: get_dictionary_object()
    # brief: We will use this to get the dictionalty object given the
    # key. Based on the type of object we will return the value of the
    # object
    #
    # param: clob - CLOB object to parse
    # param: active_key - Seems to be unused at this time ;-)
    # param: parent_key - Used to manage parent during recursion
    # param: search_parent - Parent of object to return
    # param: search_key - object key to parse. Empty will all objects
    def get_dictionary_object(self, object, active_key, parent_key, search_parent, search_key):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::get_dictionary_object()')

        # We will save the parent key so we can reset when we come back from the
        # recursive call to this method
        previous_key = parent_key

        # Note - we might want to use recussion to iterationt his stuff
        # We are fun playing here

        logging.debug("Start parsing ... ")

        # We will support the following input objects
        # collections.OrderedDict
        # collections.List

        if isinstance(object, (collections.OrderedDict)):
            # The object is a collection we will continue
            # to iterate

            for key in object:
                logging.debug("index: %s", key)
                active_key = key
                next_object = object[key]

                if isinstance(next_object, (collections.OrderedDict)):
                    # The object is a collection we will use recussion
                    # to following the light
                    # We have a new parent
                    parent_key = key
                    self.get_dictionary_object(next_object, key, parent_key, search_parent, search_key)
                    parent_key = previous_key

                elif isinstance(next_object, list):
                    # Object type: <class 'list'>
                    # We will expect a list of collections.OrderedDict objects
                    # or other lists or what ???
                    # We have a new parent
                    parent_key = key
                    logging.debug("Determine the object type")

                    for item_object in next_object:
                        self.get_dictionary_object(item_object, key, parent_key, search_parent, search_key)

                    parent_key = previous_key

                else:
                    # Finally we are here in the data (key - value pairs)
                    # This is where we should go after the database table validation
                    # You will need the UUID of the target
                    # might also need to map the column names ???
                    logging.debug("Determine the object type")
                    logging.debug("Object type: %s", type(next_object))
                    logging.debug("Data value: %s", next_object)

                    logging.debug("parent_key value: %s", parent_key)
                    logging.debug("search_parent value: %s", search_parent)
                    logging.debug("active_key value: %s", active_key)
                    logging.debug("search_keyword value: %s", search_key)

                    if parent_key == search_parent:
                        if search_key:
                            # logging.debug("Parent keys match")
                            if active_key == search_key:
                                # We have a key match. We will create and set the
                                # result list
                                data_object = module_data_object.DataObject(parent_key, key, next_object)
                                self.resultList.append(data_object)
                        else:
                            # We have a key match. We will create and set the
                            # result list
                            data_object = module_data_object.DataObject(parent_key, key, next_object)
                            self.resultList.append(data_object)

        else:
            logging.debug("Object type: %s", type(object))
            logging.debug("index: %s", object)

        logging.debug("Done")
