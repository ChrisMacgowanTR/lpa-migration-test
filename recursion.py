


def get_rec_vals(self, rec, findKey, last=''):
    ret_list = []
    # ret_list = OrderedDict()
    # ret_list = pd.DataFrame()
    print('rec = ', rec)
    # for key, val in rec.items():

    for key, val in rec.items():
        print('key = ', key)
        print('val = ', val)

        if key == findKey:
            print('found key ', findKey)
            ret_list = val
            # ret_list = OrderedDict(val)
            print('ret_list = ', ret_list)
            # return OrderedDict(ret_list)
            return ret_list

        elif isinstance(val, OrderedDict):
            # recursive call
            print('in recursive call')
            # ret_list.extend(self.get_rec_vals(OrderedDict(key), findKey))
            # self.get_rec_vals(OrderedDict(val.items()), findKey)
            # yield from self.get_rec_vals(val, findKey, last = key)
            self.get_rec_vals(val, findKey, last=key)

        else:
            ret_list.append(val)
            # ret_list = val
    return ret_list


def test_orderedDictTravese(self):
    allOracle = 0

    # allOracle = loadClobValues("role_data", "lpa_test.Role",
    #                            "ROLE_UUID in ('Iaac53e00bd9a11de9b8c850332338889')")

    # allOracle.columns = ['role_data']

    # We were testing here

    # allOracle = OrderedDict(
    #     [('educations',
    #       OrderedDict([('education', [OrderedDict([('type', 'LE'), ('schoolName', 'Nicholaus Copernicus University School of Law'), ('graduationDate', '1952'), ('degreeDesc', '4a42d21a-1b45-4f46-af19-017eed023f0f'), ('city', 'Torun'), ('country', 'Poland')]),
    #                                                               OrderedDict([('type', 'NLE'), ('schoolName', '4a42d21a-1b45-4f46-af19-017eed023f0f'), ('graduationDate', '1914'), ('degreeDesc', '4a42d21a-1b45-4f46-af19-017eed023f0f'), ('city', '4a42d21a-1b45-4f46-af19-017eed023f0f'), ('state', 'South Dakota'), ('stateAbbr', 'SD'), ('country', 'United States of America')])])])),}
    # print('Oracle CLOB for Iaac53e00bd9a11de9b8c850332338889 \n', allOracle)

    for oindex, oClob in allOracle.itertuples():
        print('oindex = ', oindex)
        print('oClob = ', oClob)
        # retOclob = OrderedDict()

        retOclob = self.get_rec_vals(oClob, "educations")
        # retOclob = self.get_rec_vals(oClob, "education")
        print('retClob = ', retOclob)

        ii = 0

        for oKey, oKeyValue in retOclob:
            print('loop # = ', ii)
            print('id2 : ', oKey)
            # print('keys2', list(oKeyValue.items()))
            print('keys2', oKeyValue)
            print('number of keys', len(oKeyValue))
            ii = ii + 1

            for oKey2 in oKeyValue:
                print('oKey2 = ', oKey2)
                print('type = ', oKeyValue[oKey])

                if oKey == "ancillaryBizs":

                    print('Peace!')

                    # for oid, obiz in oValue.items():
                    #     print('value = ', obiz['value'])
                    #     oAncillaryBiz.append(obiz['value'])
                    #     print('oAncillaryBiz[0] = ', oAncillaryBiz[0])
