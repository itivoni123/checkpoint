import pytest


def pytest_addoption(parser):
    parser.addoption("--username", dest='username', action='store', default="email@gmail.com", help='Email Address')
    parser.addoption("--password", dest="password", action="store", default="your-password", help='Email Password')
    parser.addoption("--invalid_password", dest="invalid_password", action="store", default="blabla123", help='Wrong Password')
    parser.addoption("--invalid_email", dest="invalid_email", action="store", default="bla@gmail.com", help='Wrong User Name')
    parser.addoption("--base_url", dest="base_url", action="store", default="https://mail.google.com/", help='Base URL')


@pytest.fixture
def base_url(request):
    con = request.config.getoption("base_url")
    return con


@pytest.fixture
def password(request):
    pwd = request.config.getoption("password")
    return pwd


@pytest.fixture
def invalid_password(request):
    pwd = request.config.getoption("invalid_password")
    return pwd

@pytest.fixture
def username(request):
    username = request.config.getoption("username")
    return username

@pytest.fixture
def invalid_email(request):
    invalid_email = request.config.getoption("invalid_email")
    return invalid_email
