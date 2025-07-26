from playwright.async_api import BrowserContext, Browser


class BrowserContextManager:
    async def create_browser_context(self,browser:Browser)->BrowserContext:
        return await browser.new_context()

    async def close_browser_context(self,browser_context:BrowserContext)->None:
        await browser_context.close()