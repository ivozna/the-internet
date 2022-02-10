from playwright.sync_api import Playwright


class LoginPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.goto('https://the-internet.herokuapp.com/login')

    def login(self):
        self.page.fill('#username', 'tomsmith')
        self.page.fill('#password', 'SuperSecretPassword!')
        self.page.click('.fa-sign-in')

    def log_result(self, text):
        return text in self.page.inner_text('#flash-messages')

    def log_out(self):
        self.page.click('a[href="/logout"]')

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

