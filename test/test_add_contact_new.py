from model.contact import Contact

#-рабочий тест, загружает данные групп из файла json,
#-сверяет списки, загружая данные из БД
def test_add_contact_json(app, json_contacts, db, check_ui):
    contact = json_contacts
    #old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
         # удаляем лишние пробелы в списке из БД, которых не будет в интерфейсе
         new_contacts = map(app.contact.clean_spaces, db.get_contact_list())
         assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

"""
#-рабочий тест, загружает данные контактов из модуля py,
#- сверяет списки, загружая данные из интерфейса
def test_add_contact_py(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
"""
