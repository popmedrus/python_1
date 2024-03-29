from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fixture.session import SessionHelper
from fixture.user import UserHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.vars = {}
        self.session = SessionHelper(self)
        self.user = UserHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

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

    def open_home_page(self):
        self.driver.get("http://users.bugred.ru/user/login/index.html")

    def open_users_page(self):
        self.driver.get(self.base_url)

    def destroy(self):
        self.driver.quit()
