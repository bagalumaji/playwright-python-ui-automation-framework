from playwright.async_api import async_playwright, Playwright
from drivers.interfaces.iplaywright_manager import IPlaywrightManager


class PlaywrightManager(IPlaywrightManager):
    async def start(self) -> Playwright:
        return await async_playwright().start()

    async def stop(self, playwright: Playwright) -> None:
        await playwright.stop()
