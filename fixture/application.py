from selenium.webdriver.firefox.webdriver import WebDriver

#загружаем модуль для работы с селектами
from selenium.webdriver.support.ui import Select

class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def login(self, username, password):
        wd = self.wd

        #open_home_page
        wd.get("http://localhost:8080/addressbook")

        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def open_groups_page(self):
        wd = self.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()


    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def create_contact(self, contact):
        wd = self.wd
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



    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def destroy(self):
        self.wd.quit()