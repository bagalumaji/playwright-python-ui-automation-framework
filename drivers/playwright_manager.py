from playwright.async_api import async_playwright, Playwright


class PlaywrightManager:
    async def start_playwright(self):
        return await async_playwright().start()

    async def stop_playwright(self,playwright:Playwright):
        await playwright.stop()