#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    #def __init__(self, browser = "firefox"):
    def __init__(self, browser, base_url):
                #self.wd = WebDriver(capabilities={"marionette": False})
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
            #self.wd.implicitly_wait(5)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        #wd.get("http://localhost:8080/addressbook")
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()