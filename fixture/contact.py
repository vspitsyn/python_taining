#загружаем модуль для работы с селектами
import time
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()

        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[@value='Enter']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        #select_first_contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(3)

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select_first_contact
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        # init contact edition
        #wd.find_element_by_xpath("//input[@title='Edit']").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)

        # submit contact edition
        wd.find_element_by_xpath("//input[@value='Update']").click()
        time.sleep(3)

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
            selectDay1 = Select(wd.find_element_by_xpath("//select[@name='"+field_name+"']"))
            selectDay1.select_by_visible_text(text)

    def fill_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)