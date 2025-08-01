from playwright.async_api import Locator


class PageActions:
    @staticmethod
    async def click(locator: Locator) -> None:
        await locator.click()

    @staticmethod
    async def fill(locator: Locator, text: str):
        await locator.fill(text)
