# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_edit_some_group(app):
    #app.session.login("admin", "secret")
    if app.group.count() == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups = app.group.get_group_list()
    #index = 0
    index = randrange(len(old_groups))
    group = Group(name="ИУ3_test", header="HE_test", footer="IS_test", id = old_groups[index].id)
    app.group.edit_group_by_index(index, group)
    #app.group.edit_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_name_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="ИУ9"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
