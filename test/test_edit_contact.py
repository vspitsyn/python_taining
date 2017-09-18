# -*- coding: utf-8 -*-
from model.contact import Contact
import random

#-рабочий тест, сверяет списки, загружая данные из БД
def test_edit_some_contact(app,db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname  = "IVAN",
                                    middlename = "IVANOVICH",
                                    lastname = "IVANOV"))
    old_contacts = db.get_contact_list()
    contact_was = random.choice(old_contacts)
    index = old_contacts.index(contact_was)
    #create contact object
    contact_now = Contact(firstname  = "Первый5",
                        nickname = "EPI",
                        title = "Secretary",
                        company = "Sviaz-Bank",
                        company_address = "St. Novoryazanskaya, d. 31/7, korp.1, Moscow",
                        home_phone = "",
                        mobile_phone = "мобилка",
                        work_phone = "+71112223344",
                        fax = "no",
                        email2 = "not",
                        email3 = "no",
                        homepage = "www.epi100.ru",
                        birth_day = "4",
                        birth_month = "February",
                        birth_year = "1986",
                        anniver_day = "4",
                        anniver_month  ="February",
                        anniver_year = "2006",
                        home_address = "St.15 Parkovaya, D. 4, kV. 1, Moscow",
                        home_phone2 = "no",
                        notes = "two children")
    app.contact.edit_contact_by_id(contact_was.id,contact_now)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index].fill_contact_values(contact_now)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_contacts = map(app.contact.clean_spaces, db.get_contact_list())
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


"""
#-рабочий тест, сверяет списки, загружая данные из интерфейса
from random import randrange
def test_edit_some_contact(app):
    # login
    #app.session.login("admin", "secret")
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname  = "IVAN",
                                    middlename = "IVANOVICH",
                                    lastname = "IVANOV"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    #create contact object
    contact1 = Contact(firstname  = "Первый5",
                        nickname = "EPI",
                        title = "Secretary",
                        company = "Sviaz-Bank",
                        company_address = "St. Novoryazanskaya, d. 31/7, korp.1, Moscow",
                        home_phone = "",
                        mobile_phone = "мобилка",
                        work_phone = "+71112223344",
                        fax = "no",
                        email2 = "not",
                        email3 = "no",
                        homepage = "www.epi100.ru",
                        birth_day = "4",
                        birth_month = "February",
                        birth_year = "1986",
                        anniver_day = "4",
                        anniver_month  ="February",
                        anniver_year = "2006",
                        home_address = "St.15 Parkovaya, D. 4, kV. 1, Moscow",
                        home_phone2 = "no",
                        notes = "two children")
    app.contact.edit_contact_by_index(index,contact1)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index].fill_contact_values(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
"""
