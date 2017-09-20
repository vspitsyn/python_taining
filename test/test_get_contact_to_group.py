from model.contact import Contact
import random

#-рабочий тест, сверяет списки, загружая данные из БД
from random import randrange
def test_get_contact_to_group(app,db,check_ui):
    if  len(db.get_group_list()) == 0:
        app.group.create(Group(name="ИУ_Test2", header="WeTest2", footer="AreTest2"))

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname  = "IVAN2",
                                    middlename = "IVANOVICH2",
                                    lastname = "IVANOV2"))
    app.contact.select_group_contacts('151')
