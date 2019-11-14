#
# LPA Migration Test
# CLOB Parser Utility
# Chris Macgowan
# 14 Nov 2019
# clob_parser.py
#
# We will use this class to parse the clob data.
# More news at 11pm
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

    # method: run()
    # brief: Validate the data in the row with the database
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def parse(self, clob, keyword):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: CLOBParser::parse()')

        data_object = module_data_object.DataObject('key', 'value')

        self.resultList.append(data_object)
        self.resultList.append(data_object)
        self.resultList.append(data_object)

        print(json.dumps(clob, indent=2))

        # Note - we might want to use recussion to iterationt his stuff
        # We are fun playing here

        logging.debug("Start parsing ... ")

        for key in clob:
            logging.debug("index: %s", key)

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

                self.get_dictionary_object(value)
            else:
                logging.debug("Object type: %s", type(value))

        logging.debug("Done")
        return self.resultList

    # method: get_dictionary_object()
    # brief: We will use this to get the dictionalty object given the
    # key. Based on the type of object we will return the value of the
    # object
    # param: object - the data we are passing
    def get_dictionary_object(self, object):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::get_dictionary_object()')

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

                next_object = object[key]

                if isinstance(next_object, (collections.OrderedDict)):
                    # The object is a collection we will use recussion
                    # to following the light
                    self.get_dictionary_object(next_object)

                elif isinstance(next_object, list):
                    # Object type: <class 'list'>
                    # We will expect a list of collections.OrderedDict objects
                    # or other lists or what ???
                    logging.debug("Determine the object type")

                    for item_object in next_object:
                        self.get_dictionary_object(item_object)

                else:
                    # Finally we are here in the data (key - value pairs)
                    # This is where we should go after the database table validation
                    # You will need the UUID of the target
                    # might also need to map the column names ???
                    logging.debug("Determine the object type")
                    logging.debug("Object type: %s", type(next_object))
                    logging.debug("Data value: %s", next_object)
        else:
            logging.debug("Object type: %s", type(object))
            logging.debug("index: %s", object)

        logging.debug("Done")









