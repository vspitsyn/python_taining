import re
from random import randrange

#сверка информации для случайно выбранного контакта на странице контактов и на странице редактирования
def test_contact_data_on_home_page(app):
    contact_list_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contact_list_from_home_page))
    contact_from_home_page = contact_list_from_home_page[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.company_address == contact_from_edit_page.company_address
    assert contact_from_home_page.all_mail_from_home_page == merge_mail_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
def clear(s):
    return re.sub("[() -]","",s)

def merge_mail_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="", filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="", map(lambda x: clear(x),
                                                 filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone,  contact.fax]))))