# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

# def test_delete_first_contact(app):
#     #app.session.login(username="admin", password="secret")
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname  = "IVAN",
#                                     middlename = "IVANOVICH",
#                                     lastname = "IVANOV"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.delete_first_contact()
#     # сравниваем размер списков
#     assert len(old_contacts) - 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[0:1] = []
#     assert old_contacts == new_contacts
#     #app.session.logout()

def test_delete_some_contact(app):
    #app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname  = "IVAN",
                                    middlename = "IVANOVICH",
                                    lastname = "IVANOV"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    #app.contact.delete_contact_by_index(0)
    app.contact.delete_contact_by_index(index)
    # сравниваем размер списков
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    # app.session.logout()