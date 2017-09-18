# -*- coding: utf-8 -*-
from model.contact import Contact
import datetime
import model.date_time
import  pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters*15+string.digits*15+'!#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'*15+string.punctuation+" "*90
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_true_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# def random_name_string(prefix, maxlen):
#     symbols = string.ascii_letters+"- "*5
#     return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_name_string(prefix, maxlen):
    symbols = string.ascii_letters+"- "*5
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_www_true_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+"-._=+/"*5
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname  = random_name_string("first",10),
                    middlename = random_name_string("middle",10),
                    lastname = random_name_string("last",10),
                    nickname = random_string("nik",10),
                    title = random_string("title",20),
                    company = random_string("comp",20),
                    company_address = random_string("comp_addr",40),
                    home_phone = random_string("home_ph",15),
                    mobile_phone = random_string("mob_ph",15),
                    work_phone = random_string("work_ph",15),
                    fax = random_string("fax",15),
                    email1 = random_string("e1@",15),
                    email2 = random_string("e2@",15),
                    email3 = random_string("e3@",15),
                    homepage = random_www_true_string("www",15),
                    birth_date = model.date_time.randomDate(datetime.date(1900,1,1), datetime.date(2017,1,1)),
                    anniver_date = model.date_time.randomDate(datetime.date(1900,1,1), datetime.date(2017,1,1)),
                    home_address = random_string("home_addr",40),
                    home_phone2 = random_string("home_ph2",15),
                    notes = random_string("notr",40)) for i in range(4)]


@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])

def test_new_contact(app, contact):

    old_contacts = app.contact.get_contact_list()
    ##create contact object
    # contact1 = Contact(firstname  = "Elena",
    #                     middlename = "Petrovna",
    #                     lastname = "Ivanova",
    #                     nickname = "EPI",
    #                     title = "Secretary",
    #                     company = "Sviaz-Bank",
    #                     company_address = "St. Novoryazanskaya, d. 31/7, korp.1, Moscow",
    #                     home_phone = "+77776665544",
    #                     mobile_phone = "+78883332244",
    #                     work_phone = "+71112223344",
    #                     fax = "no",
    #                     email1 = "epi100@mail.ru",
    #                     email2 = "no",
    #                     email3 = "no",
    #                     homepage = "www.epi100.ru",
    #                     birth_day = "3",
    #                     birth_month = "February",
    #                     birth_year = "1986",
    #                     anniver_day = "3",
    #                     anniver_month  ="February",
    #                     anniver_year = "2006",
    #                     home_address = "St.16 Parkovaya, D. 4, kV. 1, Moscow",
    #                     home_phone2 = "no",
    #                     notes = "two children")
    #create contact
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


    # logout
    #app.session.logout()


#1