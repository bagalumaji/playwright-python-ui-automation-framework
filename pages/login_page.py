from playwright.async_api import Locator


class LoginPage:
    def __init__(self, page):
        self.page = page

    @property
    def __username_text_box(self) -> Locator:
        return self.page.locator("#user-name")

    @property
    def __password_text_box(self) -> Locator:
        return self.page.locator("#password")

    @property
    def __login_button(self) -> Locator:
        return self.page.locator('//input[@value="LOGIN"]')

    async def __enter_username(self, name: str) -> None:
        await self.__username_text_box.fill(name)

    async def __enter_password(self, password: str) -> None:
        await self.__password_text_box.fill(password)

    async def __click_on_login_button(self) -> None:
        await self.__login_button.click()

    async def login_to_application(self, username, password) -> None:
        await self.__enter_username(username)
        await self.__enter_password(password)
        await self.__click_on_login_button()
