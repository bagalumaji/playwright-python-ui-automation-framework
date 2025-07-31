from playwright.async_api import Playwright, Browser

from drivers.ibrowser import IBrowser


class WebkitBrowser(IBrowser):
    async def create_browser(self, playwright: Playwright)->Browser:
        return await playwright.webkit.launch(headless=False)
