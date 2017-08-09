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

    def delete_first_contact(self):
        wd = self.app.wd
        #select_first_contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        time.sleep(3)