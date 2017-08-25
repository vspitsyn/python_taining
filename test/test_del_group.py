# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_delete_some_group(app):
    #app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    #сравниваем размер списков
    assert len(old_groups)-1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups


