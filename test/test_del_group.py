# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    #app.session.login(username="admin", password="secret")
    if app.group.count() == 0:
        app.group.create(Group(name="ИУ_Test", header="WeTest", footer="AreTest"))
    app.group.delete_first_group()
    #app.session.logout()
