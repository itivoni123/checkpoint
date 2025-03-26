import pytest
from playwright.async_api import async_playwright


class TestGmailLogIn(object):
    options = {
        'args': ["--disable-blink-features=AutomationControlled"],
        'ignore_default_args': ["--enable-automation"],
        "headless": False
    }

    @pytest.mark.asyncio
    async def test_valid_login(self, username, password, base_url):


        async with async_playwright() as p:
            browser = await p.chromium.launch(**self.options)
            page = await browser.new_page()

            await page.goto(base_url)
            await page.fill("input[type='email']", username)
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)

            await page.fill("input[type='password']", password)
            await page.click("button:has-text('Next')")

            assert "inbox" in page.url.lower() or "challenge" in page.url.lower()
            await browser.close()


    @pytest.mark.asyncio
    async def test_invalid_password(self, base_url, username, invalid_password):
        async with async_playwright() as p:
            browser = await p.chromium.launch(**self.options)

            page = await browser.new_page()

            await page.goto(base_url)
            await page.fill("input[type='email']", username)
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)

            await page.fill("input[type='password']", invalid_password)
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)
            assert await page.is_visible("text=Wrong password. Try again or click Forgot password to reset it.")
            await browser.close()


    @pytest.mark.asyncio
    async def test_invalid_email(self, base_url, password, invalid_email):
        async with async_playwright() as p:
            browser = await p.chromium.launch(**self.options)

            page = await browser.new_page()

            await page.goto(base_url)
            await page.fill("input[type='email']", invalid_email)
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)
            assert await page.is_visible("text=Couldn’t find your Google Account")
            await browser.close()


    @pytest.mark.asyncio
    async def test_empty_fields(self, base_url):
        async with async_playwright() as p:
            browser = await p.chromium.launch(**self.options)

            page = await browser.new_page()

            await page.goto(base_url)
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)
            assert await page.is_visible("text=Enter an email or phone number")

            await browser.close()

    @pytest.mark.asyncio
    async def test_capital_letters(self, base_url, password, username):
        async with async_playwright() as p:
            browser = await p.chromium.launch(**self.options)

            page = await browser.new_page()

            await page.goto(base_url)
            await page.fill("input[type='email']", username.upper())
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)

            # Check with Capital letters
            await page.fill("input[type='password']", password.upper())
            await page.click("button:has-text('Next')")
            await page.wait_for_timeout(2000)
            assert await page.is_visible("text=Wrong password. Try again or click Forgot password to reset it.")

            await browser.close()
