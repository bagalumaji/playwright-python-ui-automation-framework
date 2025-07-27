from playwright.async_api import BrowserContext, Browser

from drivers.interfaces.ibrowser_context_manager import IBrowserContextManager


class BrowserContextManager(IBrowserContextManager):
    async def create(self, browser:Browser)->BrowserContext:
        return await browser.new_context()

    async def close(self, browser_context:BrowserContext)->None:
        await browser_context.close()