#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

connectDb = MySQLdb.connect(host="localhost", 
							user="root",
							passwd="37876732",
							db="sendajax_db")


cur = connectDb.cursor()

cur.execute("INSERT INTO posts VALUES(null, 'caçador','bodyyyyy', 1)")

cur.execute("SELECT * FROM posts")

for row in cur.fetchall() :
	print row[1]