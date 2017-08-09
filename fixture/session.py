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
