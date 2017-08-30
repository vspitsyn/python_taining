class SessionHelper:
    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # open_home_page
        self.app.open_home_page()
        # wd.get("http://localhost:8080/addressbook")
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logget_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logget_in_as(self, username):
        wd = self.app.wd
        return self.get_logget_user() == username
        #return wd.find_element_by_xpath("//div/div[1]/form/b").text == "(%s)" % username
        #return wd.find_element_by_xpath("//div/div[1]/form/b").text =="(" + username +")"

    def get_logget_user(self):
        wd = self.app.wd
        #чтобы получить чистое имя пользователя, вырезаем скобки:
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logget_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logget_in():
            if self.is_logget_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)