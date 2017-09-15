# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_edit_some_group(app,db,check_ui):
    #app.session.login("admin", "secret")
    if  len(db.get_group_list()) == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups = db.get_group_list()
    group_was = random.choice(old_groups)
    index = old_groups.index(group_was)
    group_now = Group(name="ИУ3_test", header="HE_test", footer="IS_test", id = group_was.id)
    app.group.edit_group_by_id(group_was.id, group_now)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_now
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        #удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
        new_groups = map(app.group.clean_spaces, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

"""
#-рабочий тест, сверяет списки, загружая данные из интерфейса
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

"""