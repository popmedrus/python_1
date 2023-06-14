from model.user import User


def test_modify_user_name(app):
    app.user.find(User(user_name="rh22"))
    app.user.modify(User(user_name="new_rh22"))


def test_modify_user_email(app):
    app.user.find(User(user_name="new_rh22"))
    app.user.modify(User(user_email="new_rh22@gmail.com"))
