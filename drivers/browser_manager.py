from playwright.async_api import Browser, Playwright

from config.config_reader import ConfigReader
from config.iconfig_reader import IConfigReader
from drivers.interfaces.ibrowser_manager import IBrowserManager
from enums.section_types import SectionTypes


class BrowserManager(IBrowserManager):
    async def launch(self, playwright: Playwright) -> Browser:
        config: IConfigReader = ConfigReader()
        browser: str = config.get(SectionTypes.DEFAULT, "browser")
        headless_mode = config.getboolean(SectionTypes.DEFAULT, "headless")

        if browser.__eq__("chrome"):
            return await playwright.chromium.launch(headless=headless_mode, channel="chrome")
        elif browser.__eq__("edge"):
            return await playwright.chromium.launch(headless=headless_mode, channel="msedge")
        elif browser.__eq__("firefox"):
            return await playwright.firefox.launch(headless=headless_mode)
        elif browser.__eq__("webkit"):
            return await playwright.webkit.launch(headless=headless_mode)
        else:
            return await playwright.chromium.launch(headless=headless_mode)

    async def close(self, browser: Browser) -> None:
        await browser.close()
