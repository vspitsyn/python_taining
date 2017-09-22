#тянем из пони
from fixture.orm import ORMFixture
from fixture.db import DbFixture
from model.group import Group
#from model.functions import key_address_in_group

'''
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

db = DbFixture(host='localhost', name='addressbook', user='root', password= '')

try:
    groups = db.get_group_id_list_with_contact('57')
    # contacts = db.get_contact_list()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))
    #
    # contacts = db.get_contact_list_not_in_group()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))
    #
    # contacts = db.get_contact_list_in_group()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))


    address_in_group = db.get_address_in_group_list()
    # def key_address_in_group(list):
    #     return [int(list[0]),int(list[1])]
    #address_in_group_sorted = sorted(address_in_group,key=key_address_in_group)
    address_in_group_sorted = sorted(address_in_group, key=lambda x:[int(x[0]),int(x[1])] )

    for addr_in_group in address_in_group:
        print(addr_in_group[0])
        print(addr_in_group[1])
finally:
    db.destroy()

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
