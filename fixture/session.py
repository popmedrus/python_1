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
        self.app.driver.find_element(By.LINK_TEXT, "popmedrus").click()
        self.app.driver.find_element(By.LINK_TEXT, "Выход").click()
