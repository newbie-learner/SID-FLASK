import sqlite3 as sql
import time

#conn = sql.connect('AA_db.sqlite')
#cur = conn.cursor()
#cur.execute('CREATE TABLE experiments (name VARCHAR, description VARCHAR)')
#cur.execute('INSERT INTO experiments (name, description) values ("SID", "My experiment NetworkingAI")')
#cur.execute('INSERT INTO experiments (name, description) VALUES (?, ?)',
#                        ('Another User', 'Another Experiment, even using " other characters"'))
#conn.commit()
##conn.close()
#import pdb;pdb.set_trace()
def insertMAPRule(dmr=None, ipv6_fixlen=None, name=None, status=None, version=None, manufacturer_code=None, fmr=None):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO  ruleServer1(dmr, ipv6_fixlen, name, status,\
                version, manufacturer_code, fmr)\
                VALUES (?,?,?,?,?,?,?)",\
                    (dmr, ipv6_fixlen, name, status,version, manufacturer_code, fmr))
    con.commit()
    time.sleep(5)
    con.close()

def queryMAPRule(id=None):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM ruleServer1")
    #cur.execute("SELECT * FROM ruleServer1 where id=8")
    users = cur.fetchall()
    con.close()
    return users
