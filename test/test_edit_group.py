# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    #app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="ИУ8", header="HE", footer="IS"))
    #app.session.logout()

def test_edit_name_first_group(app):
    #app.session.login("admin", "secret")
    app.group.edit_first_group(Group(name="ИУ9"))
    #app.session.logout()