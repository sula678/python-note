#!/usr/bin/env python

# pip is used for query hive through hiveserver2
# pip install pyhs2

import pyhs2

# parameter 'host' is hiveserver2 server, not hive thrift server.
# use NOSAL
conn = pyhs2.connect(host='localhost', port=10000,authMechanism='NOSASL', user='neil.tu', password='',database='default')

# use LDAP
# conn = pyhs2.connect(host='localhost', port=10000,authMechanism='LDAP', user='neil.tu', password='neil.tu',database='default')

with conn.cursor() as cur:

    try:
        cur.execute("SELECT * FROM xxx_db.xxx_tbl WHERE dt='20140312' LIMIT 1")
        for result in cur.fetch():
            print result
    except:
        print 'select failed'