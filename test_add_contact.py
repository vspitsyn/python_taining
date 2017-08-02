# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

#загружаем модуль работы с селектами
from selenium.webdriver.support.ui import Select

#from selenium.webdriver.common.action_chains import ActionChains

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

    def create_contact(self, wd, firstname, middlename, lastname, nickname, title, company, company_address, home_phone,
                       mobile_phone, work_phone, fax, email1, email2, email3, homepage, birth_day, birth_month,
                       birth_year, anniver_day, anniver_month, anniver_year, home_address, address, notes):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").send_keys(nickname)
        # wd.find_element_by_name("photo").click()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").send_keys(company_address)
        wd.find_element_by_name("home").send_keys(home_phone)
        wd.find_element_by_name("mobile").send_keys(mobile_phone)
        wd.find_element_by_name("work").send_keys(work_phone)
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").send_keys(homepage)
        # Birthday date
        selectDay1 = Select(wd.find_element_by_xpath("//select[@name='bday']"))
        selectDay1.select_by_visible_text(birth_day)
        selectMon1 = Select(wd.find_element_by_xpath("//select[@name='bmonth']"))
        selectMon1.select_by_visible_text(birth_month)
        wd.find_element_by_name("byear").send_keys(birth_year)
        # Anniversary date
        selectDay1 = Select(wd.find_element_by_xpath("//select[@name='aday']"))
        selectDay1.select_by_visible_text(anniver_day)
        selectMon1 = Select(wd.find_element_by_xpath("//select[@name='amonth']"))
        selectMon1.select_by_visible_text(anniver_month)
        wd.find_element_by_name("ayear").send_keys(anniver_year)

        wd.find_element_by_name("address2").send_keys(home_address)
        wd.find_element_by_name("phone2").send_keys(address)
        wd.find_element_by_name("notes").send_keys(notes)
        # submit contact creation
        wd.find_element_by_xpath("//input[@value='Enter']").click()


    def test_test_add_contact(self):
        wd = self.wd
        # login
        self.login(wd, "admin", "secret")

        self.create_contact(wd, "Elena", "Petrovna", "Ivanova", "EPI", "Secretary", "Sviaz-Bank",
                            "St. Novoryazanskaya, d. 31/7, korp.1, Moscow", "+77776665544", "+78883332244",
                            "+71112223344", "no", "epi100@mail.ru", "no", "no", "www.epi100.ru", "2", "February",
                            "1986", "2", "February", "2006", "St.16 Parkovaya, D. 4, kV. 1, Moscow",
                            "St.16 Parkovaya, D. 4, kV. 1, Moscow", "two children")

        #logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
