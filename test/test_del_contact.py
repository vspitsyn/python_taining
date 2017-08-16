# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    #app.session.login(username="admin", password="secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname  = "IVAN",
                                    middlename = "IVANOVICH",
                                    lastname = "IVANOV"))
    app.contact.delete_first_contact()
    #app.session.logout()