from model.user import User


def test_modify_user_name(app):
    if app.user.find(User(user_name="rh23")) is None:
        app.user.create(User(user_name="rh23", user_email="rh23@gmail.com", user_password="12345678"))
    app.user.modify(User(user_name="new_rh23"))


def test_modify_user_email(app):
    app.user.find(User(user_name="new_rh22"))
    app.user.modify(User(user_email="new_rh22@gmail.com"))
