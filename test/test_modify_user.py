from model.user import User


def test_modify_user_name(app):
    app.session.login(login_login="popmedrus@gmail.com", login_password="12345678")
    app.user.find(User(user_name="rh22"))
    app.user.modify(User(user_name="new_rh22"))
    app.session.logout()


def test_modify_user_email(app):
    app.session.login(login_login="popmedrus@gmail.com", login_password="12345678")
    app.user.find(User(user_name="new_rh22"))
    app.user.modify(User(user_email="new_rh22@gmail.com"))
    app.session.logout()
