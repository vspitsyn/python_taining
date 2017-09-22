#загружаем модуль для работы с селектами
import time
import model.date_time
import re
from selenium.webdriver.support.ui import Select
from model.contact import Contact
from model.functions import clear_double_space

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add"))>0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()

        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[@value='Enter']").click()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//input[@id='%s']" % id).is_selected():
            wd.find_element_by_xpath("//input[@id='%s']" % id).click()

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_contact_page()
        #select_first_contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(3)
        self.contact_cache = None

    def delete_contact_by_id(self,id):
        wd = self.app.wd
        self.open_contact_page()
        if not wd.find_element_by_xpath("//input[@id='%s']"%id).is_selected():
            wd.find_element_by_xpath("//input[@id='%s']"%id).click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(3)
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        time.sleep(3)
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # выбираем контакт
        if not wd.find_elements_by_name("selected[]")[index].is_selected():
            wd.find_elements_by_name("selected[]")[index].click()
        # init contact edition
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        time.sleep(3)
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # выбираем контакт
        if not wd.find_element_by_xpath("//input[@id='%s']"%id).is_selected():
            wd.find_element_by_xpath("//input[@id='%s']"%id).click()
        # init contact edition
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']/img[@title='Edit']"%id).click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # выбираем контакт
        if not wd.find_elements_by_name("selected[]")[index].is_selected():
            wd.find_elements_by_name("selected[]")[index].click()
        # init contact edition
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fill_field_value("firstname",contact.firstname)
        self.fill_field_value("middlename",contact.middlename)
        self.fill_field_value("lastname",contact.lastname)
        self.fill_field_value("nickname",contact.nickname)
        # wd.find_element_by_name("photo").click()
        self.fill_field_value("title",contact.title)
        self.fill_field_value("company",contact.company)
        self.fill_field_value("address",contact.company_address)
        self.fill_field_value("home",contact.home_phone)
        self.fill_field_value("mobile",contact.mobile_phone)
        self.fill_field_value("work",contact.work_phone)
        self.fill_field_value("fax",contact.fax)
        self.fill_field_value("email",contact.email1)
        self.fill_field_value("email2",contact.email2)
        self.fill_field_value("email3",contact.email3)
        self.fill_field_value("homepage",contact.homepage)
        # Birthday date
        if contact.birth_date is not None:
            self.fill_select_value("bday",str(contact.birth_date.day))
            self.fill_select_value("bmonth", str(model.date_time.month_name(contact.birth_date.month)))
            self.fill_field_value("byear", str(contact.birth_date.year))
        else:
            self.fill_select_value("bday", str(contact.birth_day))
            self.fill_select_value("bmonth",str(contact.birth_month))
            self.fill_field_value("byear",str(contact.birth_year))
        # Anniversary date
        if contact.anniver_date is not None:
            self.fill_select_value("aday", str(contact.anniver_date.day))
            self.fill_select_value("amonth", str(model.date_time.month_name(contact.anniver_date.month)))
            self.fill_field_value("ayear", str(contact.anniver_date.year))
        else:
            self.fill_select_value("aday", str(contact.anniver_day))
            self.fill_select_value("amonth", str(contact.anniver_month))
            self.fill_field_value("ayear",str(contact.anniver_year))
        self.fill_field_value("address2",contact.home_address)
        self.fill_field_value("phone2",contact.home_phone2)
        self.fill_field_value("notes",contact.notes)

    def fill_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            #selectDay1 = Select(wd.find_element_by_xpath("//select[@name='"+field_name+"']"))
            selectDay1 = Select(wd.find_element_by_xpath("//select[@name='%s']"%field_name))
            selectDay1.select_by_visible_text(text)

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        #len(wd.find_elements_by_name("selected[]"))
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                  id = element.find_element_by_name("selected[]").get_attribute("value")
                  cells = element.find_elements_by_tag_name("td")
                  lastname = cells[1].text
                  firstname = cells[2].text
                  company_address = cells[3].text
                  all_mail = cells[4].text
                  all_phones = cells[5].text
                  #all_phones = cells[5].text.splitlines()
                  hash = lastname + firstname + cells[3].text + cells[4].text + cells[5].text
                  self.contact_cache.append(
                      Contact(lastname=lastname, firstname=firstname, id=id,company_address = company_address,
                              all_mail_from_home_page = all_mail, all_phones_from_home_page=all_phones, hash=hash))
                  #self.contact_cache.append(Contact(lastname = lastname, firstname = firstname, id = id, home_phone=all_phones[0], mobile_phone=all_phones[1], work_phone = all_phones[2], fax = all_phones[3], hash = hash))
    #              self.contact_cache.append(Contact(lastname=cells[2].text, firstname=cells[1].text, id=id))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        company_address = wd.find_element_by_name('address').get_attribute("value")
        home_phone = wd.find_element_by_name('home').get_attribute("value")
        mobile_phone = wd.find_element_by_name('mobile').get_attribute("value")
        work_phone = wd.find_element_by_name('work').get_attribute("value")
        fax = wd.find_element_by_name('fax').get_attribute("value")
        email1 = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id = id, company_address = company_address,
                       email1 = email1, email2 = email2, email3 = email3,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, fax=fax)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)",text).group(1)
        mobile_phone = re.search("M: (.*)",text).group(1)
        work_phone = re.search("W: (.*)",text).group(1)
        fax = re.search("F: (.*)",text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, fax=fax)

    #ф-я возвращает объект контакт с удаленными крайними проблеами и повторяющимеся пробелами в имени и фамилии
    def clean_spaces(self, contact):
        return Contact(id = contact.id,
                       firstname = clear_double_space(contact.firstname).strip(),
                       lastname = clear_double_space(contact.lastname).strip(),
                       nickname = clear_double_space(contact.nickname).strip(),
                       company_address=clear_double_space(contact.company_address).strip(),
                       home_phone=clear_double_space(contact.home_phone).strip(),
                       mobile_phone=clear_double_space(contact.mobile_phone).strip(),
                       work_phone=clear_double_space(contact.work_phone).strip(),
                       home_phone2=clear_double_space(contact.home_phone2).strip(),
                       email1=clear_double_space(contact.email1).strip(),
                       email2=clear_double_space(contact.email2).strip(),
                       email3=clear_double_space(contact.email3).strip())

    def append_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contact_id)
        select_name = 'to_group'
        select = Select(wd.find_element_by_xpath("//select[@name='%s']" % select_name))
        # selectDay1.select_by_visible_text('IU6_const')
        select.select_by_value(group_id)
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        #wd.switch_to_alert().accept()
        time.sleep(3)
        self.open_contact_page()

    def del_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        select_name = 'group'
        select = Select(wd.find_element_by_xpath("//select[@name='%s']" % select_name))
        # selectDay1.select_by_visible_text('IU6_const')
        select.select_by_value(group_id)
        time.sleep(3)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//input[@name='remove']").click()
        #wd.switch_to_alert().accept()
        time.sleep(3)
        self.open_contact_page()


    def select_group_contacts(self, group_id):
        wd = self.app.wd
        self.open_contact_page()
        select_name = 'to_group'
        selectDay1 = Select(wd.find_element_by_xpath("//select[@name='%s']" % select_name))
        #selectDay1.select_by_visible_text('IU6_const')
        selectDay1.select_by_value(group_id)
        #print()


