# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_some_group(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    old_groups  = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        #удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
        new_groups = map(app.group.clean_spaces, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


"""
from random import randrange
#-рабочий тест, сверяет списки, загружая данные из интерфейса
def test_delete_some_group(app):
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
"""

