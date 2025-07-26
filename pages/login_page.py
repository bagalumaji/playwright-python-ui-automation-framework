from playwright.async_api import Locator


class LoginPage:
    def __init__(self, page):
        self.page = page

    @property
    def username_text_box(self) -> Locator:
        return self.page.locator("#user-name")

    @property
    def password_text_box(self) -> Locator:
        return self.page.locator("#password")

    @property
    def login_button(self) -> Locator:
        return self.page.locator('//input[@value="LOGIN"]')

    async def enter_username(self, name: str):
        await self.username_text_box.fill(name)

    async def enter_password(self, password: str):
        await self.password_text_box.fill(password)

    async def click_on_login_button(self):
        await self.login_button.click()
