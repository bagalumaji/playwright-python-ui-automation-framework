from playwright.async_api import Playwright, Browser

from drivers.ibrowser import IBrowser


class FirefoxBrowser(IBrowser):
    async def create_browser(self, playwright: Playwright)->Browser:
        return await playwright.firefox.launch(headless=False)
