# -*- coding: utf-8 -*-
from model.contact import Contact
import model.date_time
import datetime
import random
import string
import os.path
#import json
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int (a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters*15+string.digits*15+'!#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'*15+string.punctuation+" "*90
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_true_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_name_string(prefix, maxlen):
    symbols = string.ascii_letters+"- "*5
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_www_true_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+"-._=+/"*5
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname  = random_name_string("Первыйfirst",10),
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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w", encoding='utf8') as out:
    #out.write(json.dumps(testdata, default = lambda x: x.__dict__, indent = 2))
    jsonpickle.set_encoder_options("json", ensure_ascii=False, indent = 2)
    #jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
