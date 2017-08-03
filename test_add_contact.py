# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

#загружаем модуль для работы с селектами
from selenium.webdriver.support.ui import Select

from contact import Contact

import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd =  WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def login(self, wd, username, password):
        wd.get("http://localhost:8080/addressbook")
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, wd, contact):
        # init contact creation
        wd.find_element_by_link_text("add new").click()

        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # wd.find_element_by_name("photo").click()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.company_address)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
            # Birthday date
        selectDay1 = Select(wd.find_element_by_xpath("//select[@name='bday']"))
        selectDay1.select_by_visible_text(contact.birth_day)
        selectMon1 = Select(wd.find_element_by_xpath("//select[@name='bmonth']"))
        selectMon1.select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
            # Anniversary date
        selectDay1 = Select(wd.find_element_by_xpath("//select[@name='aday']"))
        selectDay1.select_by_visible_text(contact.anniver_day)
        selectMon1 = Select(wd.find_element_by_xpath("//select[@name='amonth']"))
        selectMon1.select_by_visible_text(contact.anniver_month)
        wd.find_element_by_name("ayear").send_keys(contact.anniver_year)

        wd.find_element_by_name("address2").send_keys(contact.home_address)
        wd.find_element_by_name("phone2").send_keys(contact.home_phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)

        # submit contact creation
        wd.find_element_by_xpath("//input[@value='Enter']").click()


    def test_new_contact(self):
        wd = self.wd
        # login
        self.login(wd, "admin", "secret")

        #create contact object
        contact1 = Contact(firstname  = "Elena",
                          middlename = "Petrovna",
                          lastname = "Ivanova",
                          nickname = "EPI",
                          title = "Secretary",
                          company = "Sviaz-Bank",
                          company_address = "St. Novoryazanskaya, d. 31/7, korp.1, Moscow",
                          home_phone = "+77776665544",
                          mobile_phone = "+78883332244",
                          work_phone = "+71112223344",
                          fax = "no",
                          email1 = "epi100@mail.ru",
                          email2 = "no",
                          email3 = "no",
                          homepage = "www.epi100.ru",
                          birth_day = "3",
                          birth_month = "February",
                          birth_year = "1986",
                          anniver_day = "3",
                          anniver_month  ="February",
                          anniver_year = "2006",
                          home_address = "St.16 Parkovaya, D. 4, kV. 1, Moscow",
                          home_phone2 = "no",
                          notes = "two children")
        #create contact
        self.create_contact(wd, contact1)

        #logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
