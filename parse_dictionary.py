#
# LPA Migration Test
# Parse Dictionary
# Chris Macgowan
# 05 Nov 2019
# parse_dictionary.py
#
# We will use this class to perform the id analysis.
# More news to follow
#
import collections
import datetime
import logging
import json

import traceback
from pprint import pprint
from typing import OrderedDict


class ParseDictionary:

    # method: ParseDictionary()
    # brief: This would be the famous constructor
    # param: name - the name of the house you want
    # param: age - the age of the house you want
    def __init__(self):
        logging.debug('Inside: ParseDictionary::ParseDictionary()')

    # method: run()
    # brief: Validate the data in the row with the database
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run(self):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::run()')
        logging.debug("Loading the data file")

        Version = dict(version1 = {'Prod': '1.1'},
                       version2 = {'Unit': '12.9'},
                       version3 = {'Test': '12.8'})

        D = dict(emp1 = {'name': 'Bob', 'job': 'Mgr', 'version': Version},
                 emp2 = {'name': 'Kim', 'job': 'Dev', 'version': Version},
                 emp3 = {'name': 'Sam', 'job': 'Dev', 'version': Version})
        print(D)


    # method: run2()
    # brief: Validate the data in the row with the database
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run2(self):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::run()')
        logging.debug("Loading the data file")

        # allOracle = OrderedDict(
        #    [('educations', OrderedDict([('education', [OrderedDict([('type', 'LE'), ('schoolName', 'Nicholaus Law')]),
        #                                               OrderedDict([('type', 'NLE'), ('schoolName', 'Blue Law')])])])),}
        # print('Oracle CLOB for Iaac53e00bd9a11de9b8c850332338889 \n', allOracle)


        #allOracle = OrderedDict([('educations', OrderedDict([('education', [OrderedDict([('type', 'LE'), ('schoolName', 'Nicholaus'), ('Date', '1952'),]

        # working
        allOracle = OrderedDict([('education', 'yes')])

        hello = OrderedDict([('hello', '1')])
        hello2 = OrderedDict([('hello', '2')])
        hello3 = OrderedDict([('hello', '3')])

        # working
        allOracle3 = OrderedDict([('educations', OrderedDict([('type', 'LE'), ('education', 'blue'), ('hum', hello)])  )])

        # working
        education = OrderedDict([('type', 'LE'), ('education', 'RED')])
        allOracle4 = OrderedDict([('educations', OrderedDict([('education', education), ('color', 'blue'), ('hum', hello)])  )])

        allOracle5 = OrderedDict([('educations', OrderedDict([('education', [OrderedDict([('hello', '1')]), OrderedDict([('hello', '2')])    ]  )])  )])

        #allOracle4 = OrderedDict([('educations', OrderedDict([('type', 'LE'), ('education', 'blue')]) , OrderedDict([('type', 'LE'), ('education', 'blue')])  )])

        # pprint(allOracle3, indent=4)
        # ^ugly

        print(json.dumps(allOracle5, indent=2))
        # ^nice

        logging.debug("Done")


    # method: run3()
    # brief: Validate the data in the row with the database
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run3(self):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::run()')
        logging.debug("Loading the data file")

        # Phone Data
        phone01 = OrderedDict([('id', '1'), ('phoneNumber', '(605) 336-2880'), ('isInherited', 'Y')])
        phones = OrderedDict([('phone', phone01)])

        # Email Data
        email01 = OrderedDict([('id', '1'), ('address', 'lawyers@dehs.com'), ('isInherited', 'Y')])
        emails = OrderedDict([('email', email01)])

        # Education data
        education01 = OrderedDict([('type', 'LE'), ('schoolName', 'Nicholaus Copernicus'), ('graduationDate', '1952')])
        education02 = OrderedDict([('type', 'LW'), ('schoolName', 'Happy LAw School'), ('graduationDate', '1991')])
        education03 = OrderedDict([('type', 'LQ'), ('schoolName', 'Law School Number 1'), ('graduationDate', '1911')])
        educations = OrderedDict([('education', [education01, education02, education03   ]   )])

        allOracle88 = OrderedDict([('arbitrator', OrderedDict([('profileUuid', 'Iaac53e00bd9a11de9b8c850332338889'),
                                                               ('phones', phones),
                                                               ('emails', emails),
                                                               ('educations', educations),
                                                               ('statusType', 'A') ])  )])

        print(json.dumps(allOracle88, indent=2))

        # Note - we might want to use recussion to iterationt his stuff
        # We are fun playing here

        logging.debug("Start parsing ... ")

        for key in allOracle88:
            logging.debug("index: %s", key)

            value = allOracle88[key]

            # test the value of the object
            # if the value is a collections.OrderedDict we will
            # iterate on the object again - this is where the recussion can come in

            logging.debug("Determine the object type")
            logging.debug("Object type: %s", type(value))
            logging.debug("Data value: %s", value)

            if isinstance(value, (collections.OrderedDict)):
                # The object is a collection we will continuie
                # to iterate

                for key in value:
                    logging.debug("index: %s", key)

                    value = value[key]
                    logging.debug("Determine the object type")
                    logging.debug("Object type: %s", type(value))
                    logging.debug("Data value: %s", value)


        logging.debug("Done")



    # method: run4()
    # brief: Test the iteration of the dataset
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run4(self):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::run()')
        logging.debug("Loading the data file")

        # Phone Data
        phone01 = OrderedDict([('id', '1'), ('phoneNumber', '(605) 336-2880'), ('isInherited', 'Y')])
        phones = OrderedDict([('phone', phone01)])

        # Email Data
        email01 = OrderedDict([('id', '1'), ('address', 'lawyers@dehs.com'), ('isInherited', 'Y')])
        emails = OrderedDict([('email', email01)])

        # Education data
        education01 = OrderedDict([('type', 'LE'), ('schoolName', 'Nicholaus Copernicus'), ('graduationDate', '1952')])
        education02 = OrderedDict([('type', 'LW'), ('schoolName', 'Happy LAw School'), ('graduationDate', '1991')])
        education03 = OrderedDict([('type', 'LQ'), ('schoolName', 'Law School Number 1'), ('graduationDate', '1911')])
        educations = OrderedDict([('education', [education01, education02, education03   ]   )])

        allOracle88 = OrderedDict([('arbitrator', OrderedDict([('profileUuid', 'Iaac53e00bd9a11de9b8c850332338889'),
                                                               ('phones', phones),
                                                               ('emails', emails),
                                                               ('educations', educations),
                                                               ('statusType', 'A') ])  )])

        print(json.dumps(allOracle88, indent=2))

        # Note - we might want to use recussion to iterationt his stuff
        # We are fun playing here

        logging.debug("Start parsing ... ")

        for key in allOracle88:
            logging.debug("index: %s", key)

            value = allOracle88[key]

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

                elif isinstance(next_object, (collections.List)):
                    logging.debug("Determine the object type")
                    logging.debug("Determine the object type")

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









