#
# LPA-ACORN Migration Test Tools
# CLOB Parser Utility
# Unit Tests (using pytest)
# Chris Macgowan
# 18 Nov 2019
# test_clob_parser.py
#
# The unit tests implemented below will test the CLOB Parser's ability to
# parse the CLOB object. We will test different use cases. The CLOB test
# data is built in the
#
# Note: These tests run successfully, but when you run the entire suite
# then they fail with the result_list seems to be accumulating.
#

import logging
import json

import clob_parser as module_clob_parser
from typing import OrderedDict


# method: create_clob_data_object()
# brief: This method is called from the unit test method to setup the CLOB data
# structure.
#
# return: The CLOB Object
def create_clob_data_object():
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

    clob_object = OrderedDict([('arbitrator', OrderedDict([('profileUuid', 'Iaac53e00bd9a11de9b8c850332338889'),
                                                           ('phones', phones),
                                                           ('emails', emails),
                                                           ('educations', educations),
                                                           ('statusType', 'A')]))])

    # print(json.dumps(clob_object, indent=2))
    return clob_object

# method: test_arbitrator_profileUuid_case()
# brief: This unit test will test the CLOB Parser and access to a single object
# using the parent and key of the target object. We are testing getting the
# first object in the CLOB object from the root level.
def test_arbitrator_profileUuid_case():

    # Create the CLOB Parser object
    clob_parser = module_clob_parser.CLOBParser()

    # Get the test data object
    clob_object = create_clob_data_object()

    # Set parent and keyword for the parse operation
    search_parent = 'arbitrator'
    search_key = 'profileUuid'

    # Execute the parse operation
    result_list = clob_parser.parse(clob_object, search_parent, search_key)

    print('*********************************************')
    print('Inside: test_arbitrator_profileUuid_case() - 1')
    print('result_list length: ', len(result_list))

    result = result_list[0]
    assert len(result_list) == 1
    assert result.get_parent() == 'arbitrator'
    assert result.get_key() == 'profileUuid'
    assert result.get_value() == 'Iaac53e00bd9a11de9b8c850332338889'


# method: test_arbitrator_statusType_case()
# brief: This unit test will test the CLOB Parser and access to a single object
# using the parent and key of the target object. We are testing getting the
# last object in the CLOB object from the root level.
def test_arbitrator_statusType_case():

    # Create the CLOB Parser object
    clob_parser = module_clob_parser.CLOBParser()

    # Get the test data object
    clob_object = create_clob_data_object()

    # Set parent and keyword for the parse operation
    search_parent = 'arbitrator'
    search_key = 'statusType'

    # Execute the parse operation
    result_list = clob_parser.parse(clob_object, search_parent, search_key)

    print('*********************************************')
    print('Inside: test_arbitrator_profileUuid_case() - 1')
    print('result_list length: ', len(result_list))


    # Validation
    result = result_list[0]
    assert len(result_list) == 1
    assert result.get_parent() == 'arbitrator'
    assert result.get_key() == 'statusType'
    assert result.get_value() == 'A'


# method: test_phone_case()
# brief: This unit test will test the CLOB Parser and access to a single object
# using the parent and key of the target object. We are testing getting the
# phone object and all of it's children.
def test_phone_case():

    # Create the CLOB Parser object
    clob_parser = module_clob_parser.CLOBParser()

    # Get the test data object
    clob_object = create_clob_data_object()

    # Set parent and keyword for the parse operation
    search_parent = 'phone'
    search_key = ''

    # Execute the parse operation
    result_list = clob_parser.parse(clob_object, search_parent, search_key)

    print('*********************************************')
    print('Inside: test_arbitrator_profileUuid_case() - 3')
    print('result_list length: ', len(result_list))

    # Validation
    result = result_list[0]
    assert len(result_list) == 3
    assert result.get_parent() == 'phone'
    assert result.get_key() == 'id'
    assert result.get_value() == '1'

    result = result_list[1]
    assert result.get_parent() == 'phone'
    assert result.get_key() == 'phoneNumber'
    assert result.get_value() == '(605) 336-2880'

    result = result_list[2]
    assert result.get_parent() == 'phone'
    assert result.get_key() == 'isInherited'
    assert result.get_value() == 'Y'


# method: test_phone_case()
# brief: This unit test will test the CLOB Parser and access to a single object
# using the parent and key of the target object. We are testing getting the
# phone object and one specific child object using the key.
def test_phone_id_case():

    # Create the CLOB Parser object
    clob_parser = module_clob_parser.CLOBParser()

    # Get the test data object
    clob_object = create_clob_data_object()

    # Set parent and keyword for the parse operation
    search_parent = 'phone'
    search_key = 'id'

    # Execute the parse operation
    result_list = clob_parser.parse(clob_object, search_parent, search_key)

    print('*********************************************')
    print('Inside: test_arbitrator_profileUuid_case() - 1')
    print('result_list length: ', len(result_list))

    # Validation
    result = result_list[0]
    assert len(result_list) == 1
    assert result.get_parent() == 'phone'
    assert result.get_key() == 'id'
    assert result.get_value() == '1'


# method: test_education_case()
# brief: This unit test will test the CLOB Parser and access to a single object
# using the parent and key of the target object. We are testing getting the
# education object and all of it's children. This test case will provide
# access to a list
def test_education_case():

    # Create the CLOB Parser object
    clob_parser = module_clob_parser.CLOBParser()

    # Get the test data object
    clob_object = create_clob_data_object()

    # Set parent and keyword for the parse operation
    search_parent = 'education'
    search_key = ''

    # Execute the parse operation
    result_list = clob_parser.parse(clob_object, search_parent, search_key)

    print('*********************************************')
    print('Inside: test_arbitrator_profileUuid_case() - 9')
    print('result_list length: ', len(result_list))

    # Validation
    # Collection
    result = result_list[0]
    assert len(result_list) == 9
    assert result.get_parent() == 'education'
    assert result.get_key() == 'type'
    assert result.get_value() == 'LE'

    result = result_list[1]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'schoolName'
    assert result.get_value() == 'Nicholaus Copernicus'

    result = result_list[2]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'graduationDate'
    assert result.get_value() == '1952'

    # Collection
    result = result_list[3]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'type'
    assert result.get_value() == 'LW'

    result = result_list[4]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'schoolName'
    assert result.get_value() == 'Happy LAw School'

    result = result_list[5]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'graduationDate'
    assert result.get_value() == '1991'

    # Collection
    result = result_list[6]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'type'
    assert result.get_value() == 'LQ'

    result = result_list[7]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'schoolName'
    assert result.get_value() == 'Law School Number 1'

    result = result_list[8]
    assert result.get_parent() == 'education'
    assert result.get_key() == 'graduationDate'
    assert result.get_value() == '1911'
