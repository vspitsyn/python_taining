from model.contact import Contact
from model.group import Group
import random

#-рабочий тест, сверяет списки, загружая данные из БД
from random import randrange
def test_del_contact_from_group(app,db,check_ui):
    if  len(db.get_group_list()) == 0:
        app.group.create(Group(name="ИУ_Test2", header="WeTest2", footer="AreTest2"))

    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname  = "IVAN2",
                                    middlename = "IVANOVICH2",
                                    lastname = "IVANOV2"))

#если нет контактов в группах, то добавляем
    if len(db.get_contact_list_not_in_group()) == len(db.get_contact_list()):
        old_free_contacts = db.get_contact_list_not_in_group()
        groups = db.get_group_list()
        #контакт, который добавляем
        contact_for_group = random.choice(old_free_contacts)
        #группа, в которую добавляем
        group_for_contact = random.choice(groups)
        #добавляем контакт в группу
        app.contact.append_contact_to_group(contact_for_group.id,group_for_contact.id)
    # старый список контактов
    old_contacts = db.get_contact_list()
    #старый список связей групп и контактов
    old_address_in_group_list = db.get_address_in_group_list()
    #список контактов, состоящих хотя бы в одной группе
    contacts_in_group = db.get_contact_list_in_group()
    #контакт, который будем удалять из группы
    contact_for_delete = random.choice(contacts_in_group)
    #список групп в которых состоит контакт
    groups_with_contact = db.get_group_id_list_with_contact(contact_for_delete.id)
    id_group_for_delete = random.choice(groups_with_contact)
    index = old_address_in_group_list.index([contact_for_delete.id, id_group_for_delete])
    # удаляем контакт их группы
    app.contact.del_contact_from_group(contact_for_delete.id, id_group_for_delete)
    old_address_in_group_list[index:index + 1] = []
    new_address_in_group_list = db.get_address_in_group_list()
    new_contacts = db.get_contact_list()
    # проверяем, что список контактов не изменился
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # проверяем, что из старого списка связей удалена наша запись
    assert sorted(old_address_in_group_list, key=lambda x: [int(x[0]), int(x[1])]) == \
           sorted(new_address_in_group_list, key=lambda x: [int(x[0]), int(x[1])])
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_contacts = map(app.contact.clean_spaces, db.get_contact_list())
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
