# -*- coding: utf-8 -*-
from model.group import Group

#import time, unittest

def test_add_group(app):
    #app.session.ensure_logout()
    #app.session.login(username="admin", password="secre")
    #app.session.ensure_login(username="admin", password="secret")
    old_groups = app.group.get_group_list()
    group = Group(name="ИУ6", header="We", footer="Are")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

