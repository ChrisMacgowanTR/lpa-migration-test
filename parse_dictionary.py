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

import clob_parser as module_clob_parser

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



    # method: run5()
    # brief: Test the iteration of the dataset
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run5(self):
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

        clob_parser = module_clob_parser.CLOBParser()

        # search_parent - is required. When found it will return all the children
        # search_keyword - will return a specific child

        # Test Case 1.0 - Pass
        # search_parent = 'arbitrator'
        # search_keyword = 'profileUuid'

        # Test Case 1.1 - Pass
        # search_parent = 'arbitrator'
        # search_keyword = 'statusType'

        # Test Case 2.0 - pass
        search_parent = 'phone'
        search_keyword = ''

        # Test Case 2.1 - pass
        search_parent = 'phone'
        search_keyword = 'id'

        # Test Case 3.0 - pass
        search_parent = 'education'
        search_keyword = ''

        result_list = clob_parser.parse(allOracle88, search_parent, search_keyword)

        # We will iterate through the collection

        logging.debug("--------------------------------------------------------------------------------")
        logging.debug("CLOB Parse Data")
        logging.debug("Parent - Key:Value")

        for result in result_list:
            result_message = f"{result.get_parent()} - {result.get_key()}:{result.get_value()}"
            logging.debug(result_message)

        logging.debug("Done")



    # method: run6()
    # brief: Test the iteration of the dataset
    # Parser Needs to Work Better !
    # We need to support getting this data structure
    # parser 4 levels deep into the mine of lobe
    # <arbitrator>
    #   <alternate>
    #     <addresses>
    #       <address>
    #         <line1>
    #         <line2>
    #         <city>
    #         <state>
    #
    # I was just looking at the clob parser. We have decided to pass in a array of stuff to
    # help with the parsing. You can see below:
    # The collection:
    # parent: --> arbitrator
    # child: --> alternate
    # subChild: --> addresses
    # subSubChild: --> address
    #
    # param: row - The row we are going to validate
    # param: age - the age of the house you want
    def run6(self):
        logging.debug('------------------------------------------------------------')
        logging.debug('Inside: ParseDictionary::run6()')
        logging.debug("Loading the data file")



        # Phone Data
        phone01 = OrderedDict([('id', '1'), ('phoneNumber', '(605) 336-2880'), ('isInherited', 'Y')])
        phones = OrderedDict([('phone', phone01)])

        # Email Data
        email01 = OrderedDict([('id', '1'), ('address', 'lawyers@dehs.com'), ('isInherited', 'Y')])
        emails = OrderedDict([('email', email01)])

        # Alternate (phones)
        # Alternate Phone Data
        alt_phone01 = OrderedDict([('id', '99'), ('phoneNumber', '(999) 888-2222'), ('isInherited', 'Y')])
        alt_phones = OrderedDict([('phone', alt_phone01)])

        # Alternate Container
        alternate = OrderedDict([('phones', alt_phones)])

        # Education data
        education01 = OrderedDict([('type', 'LE'), ('schoolName', 'Nicholaus Copernicus'), ('graduationDate', '1952')])
        education02 = OrderedDict([('type', 'LW'), ('schoolName', 'Happy LAw School'), ('graduationDate', '1991')])
        education03 = OrderedDict([('type', 'LQ'), ('schoolName', 'Law School Number 1'), ('graduationDate', '1911')])
        educations = OrderedDict([('education', [education01, education02, education03   ]   )])

        allOracle88 = OrderedDict([('arbitrator', OrderedDict([('profileUuid', 'Iaac53e00bd9a11de9b8c850332338889'),
                                                               ('phones', phones),
                                                               ('alternate', alternate),
                                                               ('emails', emails),
                                                               ('educations', educations),
                                                               ('statusType', 'A') ])  )])

        print(json.dumps(allOracle88, indent=2))

        # Note - we might want to use recussion to iterationt his stuff
        # We are fun playing here

        logging.debug("Start parsing ... ")

        clob_parser = module_clob_parser.CLOBParser()

        # search_parent - is required. When found it will return all the children
        # search_keyword - will return a specific child

        # Test Case 1.0 - Pass
        parse_context10 = OrderedDict([('parent', 'arbitrator'),
                                     ('child', 'profileUuid'),
                                     ('subChild', ''),
                                     ('subSubChild', '')])

        # Test Case 1.1 - Pass
        parse_context11 = OrderedDict([('parent', 'arbitrator'),
                                     ('child', 'statusType'),
                                     ('subChild', ''),
                                     ('subSubChild', '')])

        # Test Case 2.0 - pass
        parse_context20 = OrderedDict([('parent', 'arbitrator'),
                                     ('child', 'phones'),
                                     ('subChild', 'phone'),
                                     ('subSubChild', '')])

        # Test Case 2.1 - pass
        parse_context21 = OrderedDict([('parent', 'arbitrator'),
                                     ('child', 'phones'),
                                     ('subChild', 'phone'),
                                     ('subSubChild', 'id')])

        # Test Case 3.0 - pass
        parse_context30 = OrderedDict([('parent', 'arbitrator'),
                                     ('child', 'educations'),
                                     ('subChild', 'education'),
                                     ('subSubChild', '')])

        # Test Case 9.0 - pass
        parse_context = OrderedDict([('parent', 'arbitrator'),
                                     ('child', 'alternate'),
                                     ('subChild', 'phones'),
                                     ('subSubChild', 'phone')])

        # We are adding this parse_fields parameter
        # You can read more about this in the clob parser

        parse_fields = OrderedDict([('ID', 'id'),
                                     ('PHONE_NUMBER', 'phoneNumber'),
                                     ('IS_INHERITED', 'isInherited'),
                                     ('subSubChild', 'phone')])

        result_list = clob_parser.parse2(allOracle88, parse_context, parse_fields)

        # We will iterate through the collection

        logging.debug("--------------------------------------------------------------------------------")
        logging.debug("CLOB Parse Data")
        logging.debug("Parent - Key:Value")

        for result in result_list:
            result_message = f"{result.get_parent()} - {result.get_key()}:{result.get_value()}"
            logging.debug(result_message)

        logging.debug("Done")







