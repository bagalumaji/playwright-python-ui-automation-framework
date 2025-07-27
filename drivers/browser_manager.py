from playwright.async_api import Browser, Playwright


class BrowserManager:
    async def launch(self, playwright: Playwright) -> Browser:
        return await playwright.chromium.launch(headless=False)

    async def close(self, browser: Browser) -> None:
        await browser.close()
