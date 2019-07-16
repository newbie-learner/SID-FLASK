
from flask import Flask, render_template, jsonify
from wtforms import Form, BooleanField, StringField, PasswordField, validators

#INSERT INTO ruleServer1(dmr, ipv6_fixlen, name, status, version, fmr, manufacturer_code)
#VALUES('abc3','def3','abc4','def','abc','{"fmr":{"ipv4":"1.2.3.4/24","ea_bits":"1231323","psid":"212"}}','abc3')
#import pdb;pdb.set_trace()
#db.queryMAPRule()

app = Flask(__name__)
#import pdb;pdb.set_trace()
@app.route("/rule", methods=["POST", "GET"])
def creatrule():
    """
    Create rule via FORM: Give input following parameter
    """
    if request.method == "POST":
        dmr = request.form['dmr']
        ipv6_fixlen = request.form['ipv6_fixlen']
        name = request.form['name']
        status = request.form['status']
        version = request.form['version']
        code = request.form['code']
        fmr1 = str({"ipv4":request.form['ipv4'], 'ipv6':request.form['ipv6'],\
                    'eabit': request.form['eabit'], 'psid':request.form['psid']})
        #print(f'{dmr} {ipv6_fixlen} {name} {status} {version} {code}')
        #print(f'{fmr1}')
        print(type(fmr1))
        db.insertMAPRule("%s"%dmr, "%s"%ipv6_fixlen, "%s"%name, "%s"%status,\
                         "%s"%version ,"%s"%code ,fmr="%s"%fmr1)
    return render_template("Rule.html")

@app.route("/query",methods=["GET"])
def query(id=None):
    """
    Query Rule from database and show in FORM
    """
    val = db.queryMAPRule()
    print(val)
    for i in range(len(val)):
         print(val[i])
    return render_template("output.html", rules=val)

@app.route("/rule_json", methods=["POST"])
def rule_json():
    """
    Create and Query rule by using JSON
    """
    #import pdb;pdb.set_trace()
    req_data = request.get_json()
    dmr = req_data['dmr']
    ipv6_fixlen = req_data['ipv6_fixlen']
    name = req_data['name']
    status = req_data['status']
    version = req_data['version']
    code = req_data['code']
    fmr1 = str({"fmr":{"ipv4":req_data['fmr']['ipv4'], 'ipv6':req_data['fmr']\
                       ['ipv6'], 'eabit': req_data['fmr']['eabit'],\
                       'psid':req_data['fmr']['psid']}})
    if request.method == "POST":
         db.insertMAPRule("%s"%dmr, "%s"%ipv6_fixlen, "%s"%name, "%s"%status,\
                          "%s"%version ,"%s"%code ,fmr="%s"%fmr1)
         return "Sucessfully Posted data"


rule_dict1={}
@app.route("/query_rule", methods=['GET'])
def quer_rule():

        import yaml, ast # convert dictionary string with double qotes "{'a':1}"

        #rule_dict1={}
        val = db.queryMAPRule()
        #import pdb;pdb.set_trace()
        #return jsonify(val)
        output = jsonconv(val)
        return output

def jsonconv(val):
        jsonkey = ['id', 'dmr', 'ipv6_fixlen','name','status','version','code','fmr']
        rule_dict= {}
        for i in range(len(val)):
            dict1 = {}
            for key,value in zip(jsonkey, val[i]):
                if key!='id':
                    if key == 'fmr':
                            #import pdb;pdb.set_trace()
                            dict1[key]=value
                            value2 = json.loads(dict1[key].replace("'","\""))
                            dict1[key]=value2
                    else:
                        dict1[key]=value
            rule_dict[id(int(val[i][0]))] = dict1
        #import pdb;pdb.set_trace()
        #value = json.loads(json.dumps(rule_dict))
        print(rule_dict)
        return jsonify(rule_dict)
        #return "%s"%val

if __name__ == "__main__":
    #import pdb;pdb.set_trace()
    app.run(debug=True)

