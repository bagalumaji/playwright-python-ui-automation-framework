from playwright.async_api import Browser, Playwright


class BrowserManager:
    async def launch_browser(self, playwright: Playwright) -> Browser:
        return await playwright.chromium.launch(headless=False)

    async def close_browser(self, browser: Browser) -> None:
        await browser.close()
