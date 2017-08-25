# -*- coding: utf-8 -*-
from model.contact import Contact

def test_new_contact(app):

    old_contacts = app.contact.get_contact_list()
    #create contact object
    contact1 = Contact(firstname  = "Elena",
                        middlename = "Petrovna",
                        lastname = "Ivanova",
                        nickname = "EPI",
                        title = "Secretary",
                        company = "Sviaz-Bank",
                        company_address = "St. Novoryazanskaya, d. 31/7, korp.1, Moscow",
                        home_phone = "+77776665544",
                        mobile_phone = "+78883332244",
                        work_phone = "+71112223344",
                        fax = "no",
                        email1 = "epi100@mail.ru",
                        email2 = "no",
                        email3 = "no",
                        homepage = "www.epi100.ru",
                        birth_day = "3",
                        birth_month = "February",
                        birth_year = "1986",
                        anniver_day = "3",
                        anniver_month  ="February",
                        anniver_year = "2006",
                        home_address = "St.16 Parkovaya, D. 4, kV. 1, Moscow",
                        home_phone2 = "no",
                        notes = "two children")
    #create contact
    app.contact.create(contact1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact1)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # logout
    #app.session.logout()


1