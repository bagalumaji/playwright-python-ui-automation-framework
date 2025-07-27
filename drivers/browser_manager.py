from playwright.async_api import Browser, Playwright

from drivers.interfaces.ibrowser_manager import IBrowserManager


class BrowserManager(IBrowserManager):
    async def launch(self, playwright: Playwright) -> Browser:
        return await playwright.chromium.launch(headless=False)

    async def close(self, browser: Browser) -> None:
        await browser.close()
