from playwright.async_api import Playwright, Browser

from drivers.ibrowser import IBrowser


class EdgeBrowser(IBrowser):
    async def create_browser(self, playwright: Playwright) -> Browser:
        return await playwright.chromium.launch(headless=False, channel="msedge")
