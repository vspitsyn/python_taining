# -*- coding: utf-8 -*-
from model.contact import Contact
import random

#-рабочий тест, сверяет списки, загружая данные из БД
from random import randrange
def test_delete_some_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname  = "IVAN",
                                    middlename = "IVANOVICH",
                                    lastname = "IVANOV"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    # сравниваем размер списков
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_contacts = map(app.contact.clean_spaces, db.get_contact_list())
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



"""
#-рабочий тест, сверяет списки, загружая данные из приложения
from random import randrange
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
"""