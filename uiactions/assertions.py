from playwright.async_api import Locator, Page, expect


class Assertions:
    @staticmethod
    async def is_visible(locator: Locator) -> None:
        await expect(locator).to_be_visible()
