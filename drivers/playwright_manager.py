from playwright.async_api import async_playwright, Playwright


class PlaywrightManager:
    async def start(self)->Playwright:
        return await async_playwright().start()

    async def stop(self, playwright:Playwright)->None:
        await playwright.stop()