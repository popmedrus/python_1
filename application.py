from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "popmedrus").click()
        self.driver.find_element(By.LINK_TEXT, "Выход").click()

    def check_new_user(self):
        self.driver.find_element(By.NAME, "q").click()
        self.driver.find_element(By.NAME, "q").send_keys("rh14")
        self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Посмотреть").click()

    def create_user(self, user):
        self.driver.find_element(By.LINK_TEXT, "Добавить пользователя").click()
        self.driver.find_element(By.NAME, "noibiz_name").click()
        self.driver.find_element(By.NAME, "noibiz_name").send_keys(user.user_name)
        self.driver.find_element(By.NAME, "noibiz_email").click()
        self.driver.find_element(By.NAME, "noibiz_email").send_keys(user.user_email)
        self.driver.find_element(By.NAME, "noibiz_password").click()
        self.driver.find_element(By.NAME, "noibiz_password").send_keys(user.user_password)
        self.driver.find_element(By.NAME, "noibiz_birthday").click()
        self.driver.find_element(By.NAME, "noibiz_birthday").send_keys("0001-05-07")
        self.driver.find_element(By.NAME, "noibiz_birthday").send_keys("0019-05-07")
        self.driver.find_element(By.NAME, "noibiz_birthday").send_keys("0199-05-07")
        self.driver.find_element(By.NAME, "noibiz_birthday").send_keys("1995-05-07")
        self.driver.find_element(By.NAME, "noibiz_gender").click()
        dropdown = self.driver.find_element(By.NAME, "noibiz_gender")
        dropdown.find_element(By.XPATH, "//option[. = 'Мужской']").click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        self.driver.find_element(By.NAME, "act_create").click()
        self.check_new_user()

    def login(self, login_login, login_password):
        self.open_home_page()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.NAME, "login").send_keys(login_login)
        self.driver.find_element(By.NAME, "password").send_keys(login_password)
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn").click()

    def open_home_page(self):
        self.driver.get("http://users.bugred.ru/user/login/index.html")

    def destroy(self):
        self.driver.quit()
