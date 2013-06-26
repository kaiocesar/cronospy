#!/usr/bin/env python

# ##################################
#	@Author Kaio Cesar
#	@version 0.1 for linux
# ##################################

# Import libs
import pygtk
import gtk
import MySQLdb


# connect database
connectionDb = MySQLdb.connect(host='127.0.0.1', 
							   user='root',
							   passwd='37876732',
							   db="sendajax_db")

cursor=connectionDb.cursor()


# functions
def AddPost(cursor, title, body, status):
	query="INSERT INTO posts VALUES(null,'" + title + "','" + body + "', " + status + " );"
	try:
		cursor.execute(query)
	except MySQLdb.Warning, w:
		print w
	except MySQLdb.Error, e:
		print e



sair=None

while sair<> 's' :
	titulo=raw_input("Digite o nome: ")
	body=raw_input("Digite o texto: ")
	status=raw_input("Defina o status: ")
	AddPost(cursor, titulo, body, status)
	sair=raw_input("Deseja sair S/N: ")




#title = "primeiro titulo"

