# Generated by Selenium IDE
from model.user import User


def test_create_user(app):
    app.user.create(User(user_name="rh1", user_email="rh1@gmail.com", user_password="12345678"))


def test_check_user(app):
    app.user.check(User(user_name="rh1", user_email="", user_password=""))


  