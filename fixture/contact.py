#загружаем модуль для работы с селектами
import time
import re
from selenium.webdriver.support.ui import Select
from model.contact import Contact

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

    # def delete_first_contact(self):
    #     wd = self.app.wd
    #     self.open_contact_page()
    #     #select_first_contact
    #     wd.find_element_by_name("selected[]").click()
    #     # submit deletion
    #     wd.find_element_by_xpath("//input[@value='Delete']").click()
    #     wd.switch_to_alert().accept()
    #     time.sleep(3)
    #     self.contact_cache = None

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
        self.fill_select_value("bday",contact.birth_day)
        self.fill_select_value("bmonth",contact.birth_month)
        self.fill_field_value("byear",contact.birth_year)
        # Anniversary date
        self.fill_select_value("aday", contact.anniver_day)
        self.fill_select_value("amonth", contact.anniver_month)
        self.fill_field_value("ayear",contact.anniver_year)
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