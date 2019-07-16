import sqlite3 as sql

"""
path = "/Users/ssiddh/Flask-Save-env/Flask_Practice/Flask_Practice/LOGIN_PAGE/EX-1/SID-FLASK/DatabaseE"
sqlite_file = "%s/my_db.sqlite"%path  # Sqlite file name
table_name1 = 'my_table_1'  # name of the table to be created
table_name2 = 'my_table_2'  # name of the table to be created
new_field = 'my_column' # name of the column
field_type = 'INTEGER'  # column data type
import pdb;pdb.set_trace()
# Connecting to the database file
conn = sql.connect(sqlite_file)

# Getting database handler by cursor() function for doing operation on database
# Like (CREATE, INSERT, SELECT, UPDATE, DROP, DELETE)
#cur = conn.cursor()
"""

##### SCHEMA #####
"""
drop table if exists ruleServer1;
    create table ruleServer1 (
        id integer primary key autoincrement,
        dmr VARCHAR(500),
        ipv6_fixlen VARCHAR(500),
        name VARCHAR(500),
        status VARCHAR(500),
        version VARCHAR(500),
        manufacturer_code VARCHAR(500),
        fmr JSON,
        UNIQUE (manufacturer_code)
    );

"""
sqlite_file = 'mape.sqlite'
table_name = 'ruleserver'
id_column = 'ID' # name of the primary key column
dmr_column = 'DMR' # remote end-user ip
ipv6_fixlen = 'IPV6_FIXLEN' # Length of the address to the end-user
Name = 'NAME' # Name of the server
status = 'STATUS' # Status of the server either UP or DOWN
version = 'VERSION' # Which version of CSO using
manufacturer_code = 'MANUFACTURER_CODE' # Unique code
fmr = 'FRM' # rule query which contatin ipv4, ipv6, eabit, psid info
field_type1 = 'INTEGER' # Integer Data Type
field_type2 = 'VARCHAR' # Char data type
field_type3 = 'JSON' # Json Data Type

def createtable():
	# Create new SQLite table with 8 column
	# Creating a new SQLite table with 8 column
	conn = sql.connect(sqlite_file)
	cur = conn.cursor()
	#cur.execute('create table {tn} ({nf} {ft})'\
	#		.format(tn=table_name1, nf=new_field, ft=field_type))

	# Creating a first  table with 8 column and set 1 coumn it as PRIMARY KEY
	# note that PRIMARY KEY column must consist of unique values!
	# dt1 --> data_type, nf1 -->column name
	import pdb;pdb.set_trace()
	cur.execute('create table {tn} ({cn1} {dt1} PRIMARY KEY,\
				{cn2} {dt2}, {cn3} {dt3}, {cn4} {dt4}, {cn5} {dt5})'
			.format(tn=table_name, cn1=id_column, dt1=field_type1,\
					cn2=dmr_column, dt2=field_type2, cn3=ipv6_fixlen,\
                    dt3=field_type2, cn4=Name, dt4=field_type2, cn5=status,\
                    dt5=field_type2))

	# Add new column in table
	cur.execute('alter table {tn} add column {cn6} {dt6} DEFAULT "2.0"'.format(tn=table_name,cn6=version,dt6=field_type2))
	cur.execute('alter table {tn} add column  {cn7} {dt7}'\
             .format(tn=table_name,cn7=manufacturer_code, dt7=field_type2))
	cur.execute('alter table {tn} add column {cn8} {dt8}'.format(tn=table_name, cn8=fmr,dt8=field_type3))

	# Committing changes and closing the connection to the database file
	conn.commit()

    #cur.execute("create table {tn} {fn} {ft}".format(tn=table_name1, fn=new_field, ft=field_type))
	#cur.execute('create table %s my %s'%(table_name1, field_type))

    # For closing the database connection
	conn.close()
#import pdb;pdb.set_trace()

#op = createtable()
def insertable():
    conn = sql.connect(sqlite_file)
    cur = conn.cursor()
    import pdb;pdb.set_trace()
    # A) Inserts an ID with a specific value in a second column
    """
    cur.execute("insert into {tn} ({cn1}, {cn2}, {cn3}, {cn4}, {cn5})\
                    values ('1','2001::1/64','40','Rule1', 'UP')".format(tn=table_name,\
                    cn1=id_column,cn2=dmr_column,cn3=ipv6_fixlen,cn4=Name,cn5=status))
    """
    # B) Tries to insert an ID (if it does not exist yet)
    # with a specific value in a second column
    """
    cur.execute("insert or ignore into {tn} ( {cn1},{cn5}) values (2,'UP')".format(tn=table_name,cn1=id_column,\
                                       cn5=status))
    """
    # C) Updates the newly inserted or pre-existing entry
    cur.execute("update {tn} set {cn7}=('123') where {cn1}=(2)".format(tn=table_name,\
                                                                      cn7=manufacturer_code,\
                                                                      cn1=id_column))
    conn.commit()
    conn.close()
#insertable()

def querydatabase():
	conn = sql.connect(sqlite_file)
	cur = conn.cursor()
	# Retrieve column information
	# Every column will be represented by a tuple with the following attributes:
	# (id, name, type, notnull, default_value, primary_key)
	cur.execute('pragma table_info({})'.format(table_name))
	# collect names in a list
	#names = [tup[1] for tup in cur.fetchall()]
	names =  cur.fetchall()
	print(names)

    # 1) Contents of all columns for row that match a certain value in 1 column
	cur.execute("select * from {tn} where {cn6}=('2.0')".format(tn=table_name,\
                                                                cn6=version))

	all_rows = cur.fetchall()
	print('%s'%all_rows)
	# 2) Value of a particular column for rows that match a certain value in column_1
	cur.execute('SELECT ({cn5}) FROM {tn} WHERE {cn51}="2.0"'.\
			format(cn5=status, tn=table_name,cn51=status))
	all_rows = cur.fetchall()
	print('2):', all_rows)
	conn.close()
	"""
	# 3) Value of 2 particular columns for rows that match a certain value in 1 column
	cur.execute('SELECT {coi1},{coi2} FROM {tn} WHERE {coi1}="Hi World"'.\
			format(coi1=column_2, coi2=column_3, tn=table_name, cn=column_2))
	all_rows = c.fetchall()
	print('3):', all_rows)

	# 4) Selecting only up to 10 rows that match a certain value in 1 column
	cur.execute('SELECT * FROM {tn} WHERE {cn}="Hi World" LIMIT 10'.\
			format(tn=table_name, cn=column_2))
	ten_rows = c.fetchall()
	print('4):', ten_rows)

	# 5) Check if a certain ID exists and print its column contents
	cur.execute("SELECT * FROM {tn} WHERE {idf}={my_id}".\
			format(tn=table_name, cn=column_2, idf=id_column, my_id=some_id))
	id_exists = c.fetchone()
	if id_exists:
		print('5): {}'.format(id_exists))
	else:
		print('5): {} does not exist'.format(some_id))
	"""
querydatabase()
