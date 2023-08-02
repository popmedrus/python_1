from fixture.application import Application
import pytest


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption('--browser')
        base_url = request.config.getoption('--baseUrl')
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(login_login="popmedrus@gmail.com", login_password="12345678")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseUrl', action='store', default="http://users.bugred.ru/")