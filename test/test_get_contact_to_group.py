from model.contact import Contact
from model.group import Group
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

    if len(db.get_contact_list_not_in_group()) == 0:
        app.contact.create(Contact(firstname  = "IOAN-GROUP",
                                    middlename = "IVANOVICH-GROUP",
                                    lastname = "IVANOV-GROUP"))
    old_contacts = db.get_contact_list()
    old_free_contacts = db.get_contact_list_not_in_group()
    groups = db.get_group_list()
    #старый список связей групп и контактов
    old_address_in_group_list = db.get_address_in_group_list()
    #контакт, который добавляем
    contact_for_group = random.choice(old_free_contacts)
    #группа, в которую добавляем
    group_for_contact = random.choice(groups)
    #добавляем контакт в группу
    app.contact.append_contact_to_group(contact_for_group.id,group_for_contact.id)
    #новый список связей групп и контактов
    new_address_in_group_list = db.get_address_in_group_list()
    old_address_in_group_list.append([str(contact_for_group.id),str(group_for_contact.id)])
    new_contacts = db.get_contact_list()
    # проверяем, что список контактов не изменился
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # проверяем, что в старый список связей добавилась одна корректная запись
    assert sorted(old_address_in_group_list, key=lambda x:[int(x[0]),int(x[1])] ) == \
           sorted(new_address_in_group_list, key=lambda x:[int(x[0]),int(x[1])] )
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_contacts = map(app.contact.clean_spaces, db.get_contact_list())
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


