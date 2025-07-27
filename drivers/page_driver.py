from playwright.async_api import BrowserContext, Page


class PageDriver:
    async def create(self, browser_context: BrowserContext)->Page:
        return await browser_context.new_page()

    async def close(self, page: Page)->None:
        await page.close()
