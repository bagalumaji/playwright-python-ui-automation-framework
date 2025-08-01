from playwright.async_api import Locator

from uiactions.page_actions import PageActions


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
        await PageActions.fill(self.__username_text_box, name)

    async def __enter_password(self, password: str) -> None:
        await PageActions.fill(self.__password_text_box,password)

    async def __click_on_login_button(self) -> None:
        await PageActions.click(self.__login_button)

    async def login_to_application(self, username, password) -> None:
        await self.__enter_username(username)
        await self.__enter_password(password)
        await self.__click_on_login_button()
