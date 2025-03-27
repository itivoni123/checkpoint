import pytest
from pages.login_elements import ElementsLogInPage
from pages.login_page import LogInPage


class TestGmailLogIn(ElementsLogInPage):
    options = {
        'args': ["--disable-blink-features=AutomationControlled"],
        'ignore_default_args': ["--enable-automation"],
        "headless": False
    }

    @pytest.mark.asyncio
    async def test_valid_login(self, username, password, base_url):
        login_page = LogInPage(self.options)
        is_login = await login_page.login(username, password, base_url)
        assert "challenge" in is_login


    @pytest.mark.asyncio
    async def test_invalid_password(self, base_url, username, invalid_password):
        error_msg = "Wrong password. Try again or click Forgot password to reset it."
        login_page = LogInPage(self.options)
        is_login = await login_page.login(username, password=invalid_password, base_url=base_url, msg=error_msg)
        assert is_login


    @pytest.mark.asyncio
    async def test_invalid_email(self, base_url, password, invalid_email):
        error_msg = "Couldn’t find your Google Account"
        login_page = LogInPage(self.options)
        is_login = await login_page.login(username=invalid_email, password=password, base_url=base_url, msg=error_msg)
        assert is_login


    @pytest.mark.asyncio
    async def test_empty_fields(self, base_url):
        error_msg = "Enter an email or phone number"
        login_page = LogInPage(self.options)
        is_login = await login_page.login(username="", password="", base_url=base_url, msg=error_msg)
        assert is_login

    @pytest.mark.asyncio
    async def test_capital_letters(self, base_url, password, username):
        error_msg = "Wrong password. Try again or click Forgot password to reset it."
        login_page = LogInPage(self.options)
        is_login = await login_page.login(username.upper(), password.upper(), base_url=base_url, msg=error_msg)
        assert is_login
