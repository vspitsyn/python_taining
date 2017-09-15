 #-*- coding: utf-8 -*-
from model.group import Group

#-рабочий тест, загружает данные групп из файла json,
#-сверяет списки, загружая данные из БД
def test_add_group(app, json_groups, db,check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_groups = map(app.group.clean_spaces, db.get_group_list())
         assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

"""
#import  pytest
#import time, unittest
#@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])

#from data.groups import testdata
#-рабочий тест, загружает данные групп из модуля py,
#- сверяет списки, загружая данные из интерфейса
def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    #group = Group(name="ИУ6", header="We", footer="Are")
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

#-рабочий тест, загружает данные групп из файла json,
#-сверяет списки, загружая данные из интерфейса
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
"""