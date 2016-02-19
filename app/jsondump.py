import json
import copy
import jsonexample as jp




formtable = {"name":[u'name'],
             "gender":[u'gender'],
             "contact":[u'contact'],
             "address":[u'address']}

def is_reserved_layer(dict,reserved_word):
    for key in dict:
        if reserved_word == key[:len(reserved_word)]:
            return True
    return False

def json_reduce_layer(source,reserved_word):
    if type(source)==list:
        if is_reserved_layer(source[0],reserved_word):
            temp_dict = source.pop();
            for temp_key in temp_dict:
                source.append(temp_dict[temp_key][0])
            for item in source:
                json_reduce_layer(item,reserved_word)
        else:
            for item in source:
                json_reduce_layer(item,reserved_word)
    elif type(source)==dict:
        for key in source:
            json_reduce_layer(source[key],reserved_word)

'''
def json_reduce_layer(source, reserved_word):
    if type(source)==dict:
        for key in source:
            if(type(source[key])==list and len(source[key])==1):
                if(type(source[key][0])==dict and is_reserved_layer(source[key][0],reserved_word)):
                    temp_dict = source[key].pop()
                    for temp_key in temp_dict:
                        source[key].append(temp_dict[temp_key])
                    for item in source[key]:
                        json_reduce_layer(item, reserved_word)
    elif type(source)==list:
        for item in source:
            if(type(item)==dict):
                if is_reserved_layer(item,reserved_word):
                    #this item is a reserved_layer
                    temp_dict = source.pop(obj=list[0])
                    for key in temp_dict:
                        source.append(temp_dict[key])
        for item in source:
            json_reduce_layer(item, reserved_word)
'''


def json_reduce_structure(source):
    if type(source)==dict:
        for key in source:
            if(type(source[key])==list and len(source[key])==1):
                source[key] = source[key][0]
                json_reduce_structure(source[key])
    elif type(source)==list:
        for item in source:
            if(type(item)==dict):
                json_reduce_structure(item)

def json_write(source,list,reserved_word):
    if(len(source)==1):
        #if the source is the list item in the source list, append it to the dest list
        list.append(source[0])
    else:
        if(len(list)==0):
            #the list is empty, append a new dict to it
            dict = {}
            dict[source[0]] = []
            list.append(dict)
        else:
            #there already have a dict in the list: list[0]
            if not list[0].has_key(source[0]):
                #add key source[0] in the dict
                list[0][source[0]] = []
        json_write(source[1:],list[0][source[0]],reserved_word)


def list2json(source,reserved_word):
    '''

    :param source: a list of list
    :return: a dict which can be converted into json str use json.dumps()
    '''

    #reserved_word = 'parallel_dict'

    dest = json_gene(source,reserved_word)

    json_reduce_layer(dest,reserved_word)
    json_reduce_structure(dest)

    return dest


def json_gene(list,reserved_word):
    proto = {}
    for item in list:
        if not proto.has_key(item[0]):
            proto[item[0]] = []
        json_write(item[1:],proto[item[0]],reserved_word)
    return proto


def listequal(list1,list2):
    '''
    compare the elements in these two list
    :param list1:
    :param list2:
    :return: Ture if two list are equal
    '''
    if len(list1)!=len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
                return False
    return True


def extend(prefix, extendlist, raw):
    '''

    :param prefix: list of key, there maybe more than one item  corresponding to it
    :param extendlist:extended item will append to this list
    :param raw:patient's info comeform
    :return:
    '''
    for item in raw:
        if listequal(prefix, item[:len(prefix)]):
            extendlist.append(item)


def form2list(form,formtable,raw):
    extendlist = [];

    for item in form:
        extend(formtable[item],extendlist,raw)

    return extendlist





def process(value, attribute):
    '''

    :param value:  the value of the patient's info
    :param attribute:  something like 'mask' and so on, we return different content based on it
    :return: a string, the result of process
    '''
    if attribute == 'mask':
        return 'mask'
    else:
        return value

def retrieve(policy, raw):
    '''

    :param policy: a list to identify a item of patient's info, the policy[-1] is the attribute of the item
    :param raw: result of json2list()
    :return: return processed patient's info
    '''
    newlist = policy[:-1]
    not_found_flag = True

    for item in raw:
        if listequal(policy[:-1],item[:-1]):
            not_found_flag = False
            newlist.append(process(item[-1],policy[-1]))
            return newlist

    if not_found_flag:
        newlist.append('not found')
        return newlist


def conver(item, templist, result,reserved_word):
    '''

    :param item: list or dict to be convert
    :param templist: a temp list
    :param result: every item in result is a convert result
    :return:
    '''
    if type(item)==dict:
        for key in item:
            templist.append(key)
            conver(item[key], templist, result,reserved_word)
            templist.pop()
    elif type(item) == list:
        for i in range(len(item)):
            tempkey = reserved_word+str(i)
            templist.append(tempkey)
            conver(item[i],templist,result,reserved_word)
            templist.pop()
        #for arg in item:
            #conver(arg, templist, result)
    elif type(item) == unicode:
        templist.append(item)
        resultitem = copy.deepcopy(templist)
        result.append(resultitem)
        #print item
        templist.pop()

def json2list(jsonfile,reserved_word):
    '''

    :param jsonfile: dict come from json.dumps
    :return:a list, every item in this list is a list [key1,key2,...,keyn,value],
            it show the position of value in original json file
    '''
    result = []
    templist = []
    conver(jsonfile,templist,result,reserved_word)
    return result

def test():

    reserved_word = 'parallel_dict'
    result = json2list(jp.example,reserved_word)

    for item in result:
        print item



    policy = json2list(jp.p,reserved_word)

    for item in policy:
        print item


    for item in policy:
        print retrieve(item,result)

    listtest = ['name','gender']

    extend = form2list(listtest,formtable,result)
    print 'extended item'
    for item in extend:
        print item



def jsontest():

    json_re = jp.s
    print json.dumps(jp.s,sort_keys=True,indent=4)

    reserved_word = 'parallel_dict'

    source = json2list(jp.s,reserved_word)

    for item in source:
        print item

    dest = json_gene(source,reserved_word)




    json_reduce_layer(dest,reserved_word)
    json_reduce_structure(dest)


    sdest = json.dumps(dest,sort_keys=True,indent=4)

    print sdest



    for item in source:
        print item

    json_reduce_structure(json_re)

    sdest = json.dumps(json_re,sort_keys=True,indent=4)

    print sdest



def simplejsontest():

    testlist = []
    testlist.append([u'name', 'parallel_dict0', u'use', u'official'])
    testlist.append([u'name', 'parallel_dict0', u'given', 'parallel_dict0', u'Peter'])
    testlist.append([u'name', 'parallel_dict0', u'given', 'parallel_dict1', u'James'])
    testlist.append([u'name', 'parallel_dict0', u'fhir_comments', 'parallel_dict0', u" Peter James Chalmers, but called 'Jim' "])
    testlist.append([u'name', 'parallel_dict0', u'family', 'parallel_dict0', u'Chalmers'])
    testlist.append([u'name', 'parallel_dict1', u'use', u'usual'])
    testlist.append([u'name', 'parallel_dict1', u'given', 'parallel_dict0', u'Jim'])


    result = list2json(testlist)

    print json.dumps(result,indent=4)












if __name__ == '__main__':
    test()
    #jsontest()
    #simplejsontest()


