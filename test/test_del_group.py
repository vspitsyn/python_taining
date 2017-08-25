# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    #app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    #сравниваем размер списков
    assert len(old_groups)-1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


