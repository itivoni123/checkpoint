from playwright.async_api import async_playwright
from pages.login_elements import ElementsLogInPage


class LogInPage(ElementsLogInPage):
    def __init__(self, browser):
        self.browser = browser


    async def login(self, username, password, base_url, msg=""):

        async with async_playwright() as p:
            browser = await p.chromium.launch(**self.browser)
            page = await browser.new_page()

            await page.goto(base_url)
            if "phone number" in msg:
                await page.click(ElementsLogInPage.btn_next)
                return await page.wait_for_selector(f"//div[text()='{msg}']", timeout=5000)
            await page.fill(ElementsLogInPage.css_input_field % "email", username)
            await page.click(ElementsLogInPage.btn_next)
            await page.wait_for_timeout(2000)
            if "Google Account" in msg:
                return await page.wait_for_selector(f"//div[text()='{msg}']", timeout=5000)
            await page.fill(ElementsLogInPage.css_input_field % "password", password)
            await page.click(ElementsLogInPage.btn_next)
            await page.wait_for_timeout(2000)
            if "password" in msg:
                return await page.wait_for_selector(f"//span[text()='{msg}']", timeout=5000)
            login_url = page.url.lower()
            return login_url
