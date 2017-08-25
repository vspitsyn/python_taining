# -*- coding: utf-8 -*-
from model.contact import Contact
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
                        #middlename = "Средний3",
#                        lastname = "Petrova-Sidorova",
                        nickname = "EPI",
                        title = "Secretary",
                        company = "Sviaz-Bank",
                        company_address = "St. Novoryazanskaya, d. 31/7, korp.1, Moscow",
                        home_phone = "",
                        mobile_phone = "мобилка",
                        work_phone = "+71112223344",
                        fax = "no",
#                        email1 = "epi100@mail.ru",
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
    #app.contact.edit_first_contact(contact1)
    app.contact.edit_contact_by_index(index,contact1)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
#    old_contacts[0] = contact1
    old_contacts[index].fill_contact_values(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # contact2 = Contact(anniver_day="5",
    #                    anniver_month="January",
    #                    anniver_year="2007",
    #                    notes="three children")
    #edit contact1
    #app.contact.edit_first_contact(contact2)

    # logout
    #app.session.logout()