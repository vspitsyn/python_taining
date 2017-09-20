#тянем из пони
from fixture.orm import ORMFixture
from model.group import Group
db = ORMFixture(host='localhost', name='addressbook', user='root', password= '')

try:
    l = db.get_contacts_in_group(Group(id = '151'))
    #l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()

''' 
#тянем запросами
from fixture.db import DbFixture
db = DbFixture(host='localhost', name='addressbook', user='root', password= '')

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
'''
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
#import mysql.connector
# import pymysql.cursors
#
# #connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()
#
