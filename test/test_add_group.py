# -*- coding: utf-8 -*-
from model.group import Group

#import time, unittest

def test_add_group(app):
    #app.session.login(username="admin", password="secre")
    #app.session.login(username="admin", password="secret")
    app.group.create(Group(name="ИУ6", header="We", footer="Are"))
    #app.session.logout()


def test_add_empty_group(app):
    #app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    #app.session.logout()

