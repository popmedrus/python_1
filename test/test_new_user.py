# Generated by Selenium IDE
from model.user import User
#from sys import maxsize
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [User(user_name="", user_email="", user_password="")] + [
    User(user_name=random_string('name', 10), user_email=random_string('@email.ru', 5), user_password=random_string('password', 10))
    for i in range(5)
]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_create_user(app, user):
    old_users = app.user.get_users_list()
    app.user.create(user)
    new_users = app.user.get_users_list()
    user.id = new_users[0]
    assert len(old_users) == len(new_users)
    old_users.insert(0, user.id)
    del old_users[-1]
    #print(new_users)
    #print(old_users)
    #def id_or_max(us):
        #if us.id:
            #return int(us.id)
        #else:
            #return maxsize
    assert old_users == new_users
    #assert sorted(old_users, key=id_or_max) == sorted(new_users, key=id_or_max)


def test_check_user(app):
    app.user.check(User(user_name="rh1", user_email="", user_password=""))
