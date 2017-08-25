# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    #app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname  = "IVAN",
                                    middlename = "IVANOVICH",
                                    lastname = "IVANOV"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    # сравниваем размер списков
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
    #app.session.logout()