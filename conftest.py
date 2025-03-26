import pytest
from playwright.async_api import async_playwright


def pytest_addoption(parser):
    parser.addoption("--username", dest='username', action='store', default="itivoni@gmail.com", help='Email Address')
    parser.addoption("--password", dest="password", action="store", default="Dmdm52342466", help='Email Password')
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

@pytest.fixture(scope="class")
async def page():
    options = {
        'args': [
            "--disable-blink-features=AutomationControlled",
            "--start-maximized"
        ],
        'ignore_default_args': ["--enable-automation"],
        "headless": False
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(**options)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            viewport={"width": 1920, "height": 1080}  # Mimic real user resolution
        )
        page = await context.new_page()
        yield page
        await browser.close()
