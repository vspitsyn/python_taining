# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

testdata = [
    Group(name="", header="", footer=""),
    Group(name="IU6_const", header="We_const", footer="Are_const")
    ]


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
#     return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# testdata = [Group(name="", header="", footer=""),
#     Group(name="ИУ6", header="We", footer="Are")]+ [
#     Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
#     for i in range (3)]