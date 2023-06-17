from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, login_login, login_password):
        self.app.open_home_page()
        self.app.driver.find_element(By.NAME, "login").click()
        self.app.driver.find_element(By.NAME, "login").send_keys(login_login)
        self.app.driver.find_element(By.NAME, "password").send_keys(login_password)
        self.app.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn").click()

    def logout(self):
        self.app.driver.find_element(By.LINK_TEXT, "popmed").click()
        self.app.driver.find_element(By.LINK_TEXT, "Выход").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.driver.find_elements(By.LINK_TEXT, "Выход")) > 0

    def is_logged_in_as(self, user_name):
        return self.app.driver.find_element(By.LINK_TEXT, "popmed").text == '('+user_name+')'


    def ensure_login(self, login_login, login_password):
        if self.is_logged_in():
            if self.is_logged_in_as(login_login):
                return
            else:
                self.logout()
        self.login(login_login, login_password)





