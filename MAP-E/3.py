import json
op=[(1, '2002:1230:abc::2/64', '61', 'rule-4', 'UP', '16.02', '104',"{'fmr': \
{'ipv4': '2.2.3.5/24', 'ipv6': '20001:db8::64/50', 'eabit': '12345', 'psid': \
'0193019'}}"), (2, '2002:1230:abc::2/64', '61', 'rule-4','UP', '16.02', '105',\
"{'fmr': {'ipv4': '2.2.3.5/24', 'ipv6': '20001:db8::64/50', 'eabit': '12345',\
'psid': '0193019'}}"), (3, '2002:1230:abc::2/64', '63', 'rule-5', 'UP',\
'16.02', '106', "{'fmr': {'ipv4':'2.2.3.5/24', 'ipv6': '20001:db8::64/50',\
'eabit': '12346', 'psid': '0193019'}}"), (4, '2004:1230:abc::2/64', '64',\
'rule-6', 'UP', '16.02', '108', "{'fmr': {'ipv4': '2.2.3.5/24', 'ipv6': '20001:db8::64/50',\
'eabit': '12346', 'psid': '0193019'}}"), (5, '2009:1230:abc::2/64', '69', 'rule-9', 'UP', \
'16.02', '109', "{'fmr': {'ipv4': '2.2.9.5/24', 'ipv6': '20009:db8::64/50', 'eabit': '12349', 'psid': '0193021'}}"), (
6, '2010:1230:abc::2/64', '70', 'rule-10', 'UP', '16.02', '110', "{'fmr': {'ipv4': '2.2.9.5/24', 'ipv6': '20010:db8::64/50', 'eabit': '12350', 'psid': '0193022'}}"), (7, '2010:1230:abc::2/64', '70', 'rule-10'
, 'UP', '16.02', '111', "{'fmr': {'ipv4': '2.2.9.5/24', 'ipv6': '20010:db8::64/50', 'eabit': '12350', 'psid': '0193022'}}")]

jsonkey = ['id', 'dmr', 'ipv6_fixlen','name','status','version','code','fmr']
dict2={}
dict3={}
counter=0
def jsonify():
    for i in range(len(op)):
        dict1={}
        for key,value in zip(jsonkey, op[i]):
            if key!='id':
                dict1[key]=value
        dict2[id(int(op[i][0]))] = dict1
    return (json.loads(json.dumps(dict2)))
op = jsonify()
print(op)
