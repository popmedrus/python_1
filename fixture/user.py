from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserHelper:
    def __init__(self, app):
        self.app = app

    def check_new_user(self):
        self.app.driver.find_element(By.NAME, "q").click()
        self.app.driver.find_element(By.NAME, "q").send_keys("rh14")
        self.app.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        self.app.driver.find_element(By.LINK_TEXT, "Посмотреть").click()

    def create(self, user):
        self.app.driver.find_element(By.LINK_TEXT, "Добавить пользователя").click()
        self.app.driver.find_element(By.NAME, "noibiz_name").click()
        self.app.driver.find_element(By.NAME, "noibiz_name").send_keys(user.user_name)
        self.app.driver.find_element(By.NAME, "noibiz_email").click()
        self.app.driver.find_element(By.NAME, "noibiz_email").send_keys(user.user_email)
        self.app.driver.find_element(By.NAME, "noibiz_password").click()
        self.app.driver.find_element(By.NAME, "noibiz_password").send_keys(user.user_password)
        self.app.driver.find_element(By.NAME, "noibiz_birthday").click()
        self.app.driver.find_element(By.NAME, "noibiz_birthday").send_keys("0001-05-07")
        self.app.driver.find_element(By.NAME, "noibiz_birthday").send_keys("0019-05-07")
        self.app.driver.find_element(By.NAME, "noibiz_birthday").send_keys("0199-05-07")
        self.app.driver.find_element(By.NAME, "noibiz_birthday").send_keys("1995-05-07")
        self.app.driver.find_element(By.NAME, "noibiz_gender").click()
        dropdown = self.app.driver.find_element(By.NAME, "noibiz_gender")
        dropdown.find_element(By.XPATH, "//option[. = 'Мужской']").click()
        self.app.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.app.driver.find_element(By.NAME, "act_create").click()
        self.check_new_user()
