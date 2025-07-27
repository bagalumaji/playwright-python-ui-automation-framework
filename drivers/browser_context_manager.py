from playwright.async_api import BrowserContext, Browser


class BrowserContextManager:
    async def create(self, browser:Browser)->BrowserContext:
        return await browser.new_context()

    async def close(self, browser_context:BrowserContext)->None:
        await browser_context.close()