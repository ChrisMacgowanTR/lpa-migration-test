#
# LPA Migration Test
# CLOB Parser Utility
# Unit Tests (using pytest)
# Chris Macgowan
# 18 Nov 2019
# test_clob_parser.py
#
#

import collections
import datetime
import logging
import json

import clob_parser as module_clob_parser

import traceback
from pprint import pprint
from typing import OrderedDict

def test_arbitrator_profileUuid_case():
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
    educations = OrderedDict([('education', [education01, education02, education03])])

    allOracle88 = OrderedDict([('arbitrator', OrderedDict([('profileUuid', 'Iaac53e00bd9a11de9b8c850332338889'),
                                                           ('phones', phones),
                                                           ('emails', emails),
                                                           ('educations', educations),
                                                           ('statusType', 'A')]))])

    print(json.dumps(allOracle88, indent=2))

    # Note - we might want to use recussion to iterationt his stuff
    # We are fun playing here

    logging.debug("Start parsing ... ")
    clob_parser = module_clob_parser.CLOBParser()

    # search_parent - is required. When found it will return all the children
    # search_keyword - will return a specific child

    # Test Case 1.0 - Pass
    search_parent = 'arbitrator'
    search_keyword = 'profileUuid'

    result_list = clob_parser.parse(allOracle88, search_parent, search_keyword)

    # We will iterate through the collection

    logging.debug("--------------------------------------------------------------------------------")
    logging.debug("CLOB Parse Data")
    logging.debug("Parent - Key:Value")

    for result in result_list:
        result_message = f"{result.get_parent()} - {result.get_key()}:{result.get_value()}"
        print(result_message)


    assert result.get_parent() == 'arbitrator'
    assert result.get_key() == 'profileUuid'
    assert result.get_value() == 'Iaac53e00bd9a11de9b8c850332338889'

    logging.debug("Done")






def test_arbitrator_profileUuid_222_case():
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
    educations = OrderedDict([('education', [education01, education02, education03])])

    allOracle88 = OrderedDict([('arbitrator', OrderedDict([('profileUuid', 'Iaac53e00bd9a11de9b8c850332338889'),
                                                           ('phones', phones),
                                                           ('emails', emails),
                                                           ('educations', educations),
                                                           ('statusType', 'A')]))])

    print(json.dumps(allOracle88, indent=2))

    # Note - we might want to use recussion to iterationt his stuff
    # We are fun playing here

    logging.debug("Start parsing ... ")
    clob_parser = module_clob_parser.CLOBParser()

    # search_parent - is required. When found it will return all the children
    # search_keyword - will return a specific child

    # Test Case 1.0 - Pass
    search_parent = 'arbitrator'
    search_keyword = 'profileUuid'

    result_list = clob_parser.parse(allOracle88, search_parent, search_keyword)

    # We will iterate through the collection

    logging.debug("--------------------------------------------------------------------------------")
    logging.debug("CLOB Parse Data")
    logging.debug("Parent - Key:Value")

    for result in result_list:
        result_message = f"{result.get_parent()} - {result.get_key()}:{result.get_value()}"
        print(result_message)


    assert result.get_parent() == 'arbitrator'
    assert result.get_key() == 'profileUuid'
    assert result.get_value() == 'Iaac53e00bd9a11de9b8c850332338889'

    logging.debug("Done")
