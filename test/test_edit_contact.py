# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    # login
    app.session.login("admin", "secret")

    #create contact object
    contact1 = Contact(firstname  = "Elena",
                        middlename = "Ivanovnaa",
                        lastname = "Petrova",
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
                        birth_day = "4",
                        birth_month = "February",
                        birth_year = "1986",
                        anniver_day = "4",
                        anniver_month  ="February",
                        anniver_year = "2006",
                        home_address = "St.15 Parkovaya, D. 4, kV. 1, Moscow",
                        home_phone2 = "no",
                        notes = "two children")
    #edit contact1
    app.contact.edit_first_contact(contact1)

    # logout
    app.session.logout()
