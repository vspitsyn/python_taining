# -*- coding: utf-8 -*-
from model.group import Group

#import time, unittest

def test_add_group(app):
    #app.session.login(username="admin", password="secre")
    #app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="ИУ6", header="We", footer="Are"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    #app.session.logout()


def test_add_empty_group(app):
    #app.session.login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    #app.session.logout()

