from model.user import User


def test_modify_user_name(app):
    if app.user.find(User(user_name="rh8")) != 0:
        app.user.modify(User(user_name="new_rh8"))
    else:
        app.user.create(User(user_name="rh8", user_email="rh8@gmail.com", user_password="12345678"))
        app.user.find(User(user_name="rh8"))
        app.user.modify(User(user_name="new_rh8"))


def test_modify_user_email(app):
    app.user.find(User(user_name="new_rh22"))
    app.user.modify(User(user_email="new_rh22@gmail.com"))
