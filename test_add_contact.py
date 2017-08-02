# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
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
    
    def test_test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        #wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

        wd.find_element_by_link_text("add new").click()

        wd.find_element_by_name("firstname").send_keys("Elena")
        wd.find_element_by_name("middlename").send_keys("Petrovna")
        wd.find_element_by_name("lastname").send_keys("Ivanova")
        wd.find_element_by_name("nickname").send_keys("EPI")
        #wd.find_element_by_name("photo").click()
        wd.find_element_by_name("title").send_keys("Secretary")
        wd.find_element_by_name("company").send_keys("Sviaz-Bank")
        wd.find_element_by_name("address").send_keys("St. Novoryazanskaya, d. 31/7, korp.1, Moscow")
        wd.find_element_by_name("home").send_keys("+77776665544")
        wd.find_element_by_name("mobile").send_keys("+73332221111")
        wd.find_element_by_name("work").send_keys("+71112223344")
        wd.find_element_by_name("fax").send_keys("no")
        wd.find_element_by_name("email").send_keys("epi100@mail.ru")
        wd.find_element_by_name("email2").send_keys("no")
        wd.find_element_by_name("email3").send_keys("no")
        wd.find_element_by_name("homepage").send_keys("www.epi100.ru")

        selectElemDay1 = wd.find_element_by_xpath("//select[@name='bday']")
        selectDay1 = Select(selectElemDay1)
        selectDay1.select_by_visible_text("2")

        selectElemMon1 = wd.find_element_by_xpath("//select[@name='bmonth']")
        selectMon1 = Select(selectElemMon1)
        selectMon1.select_by_visible_text("February")

        wd.find_element_by_name("byear").send_keys("1985")

        selectElemDay1 = wd.find_element_by_xpath("//select[@name='aday']")
        selectDay1 = Select(selectElemDay1)
        selectDay1.select_by_visible_text("2")

        selectElemMon1 = wd.find_element_by_xpath("//select[@name='amonth']")
        selectMon1 = Select(selectElemMon1)
        selectMon1.select_by_visible_text("February")

        wd.find_element_by_name("ayear").send_keys("2005")

        wd.find_element_by_name("address2").send_keys("St.16 Parkovaya, D. 4, kV. 1, Moscow")
        wd.find_element_by_name("phone2").send_keys("St.16 Parkovaya, D. 4, kV. 1, Moscow")
        wd.find_element_by_name("notes").send_keys("two children")

        wd.find_element_by_xpath("//input[@value='Enter']").click()
        #wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
