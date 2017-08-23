# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    #app.session.login("admin", "secret")
    if app.group.count() == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="ИУ8", header="HE", footer="IS"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

    #app.session.logout()

def test_edit_name_first_group(app):
    #app.session.login("admin", "secret")
    if app.group.count() == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="ИУ9"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.session.logout()