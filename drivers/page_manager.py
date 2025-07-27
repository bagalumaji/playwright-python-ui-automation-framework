from playwright.async_api import BrowserContext, Page

from drivers.interfaces.ipage_manager import IPageManager


class PageManager(IPageManager):
    async def create(self, browser_context: BrowserContext)->Page:
        return await browser_context.new_page()

    async def close(self, page: Page)->None:
        await page.close()
