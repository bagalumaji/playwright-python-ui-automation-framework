from playwright.async_api import Browser

from config.config_reader import ConfigReader
from config.iconfig_reader import IConfigReader
from drivers.browser_factory import BrowserFactory
from drivers.ibrowser import IBrowser
from drivers.interfaces.ibrowser_manager import IBrowserManager
from enums.section_types import SectionTypes


class BrowserManager(IBrowserManager):
    async def launch(self) -> IBrowser:
        config: IConfigReader = ConfigReader()
        browser_name = config.get(SectionTypes.DEFAULT, "browser").lower()
        headless_mode = config.getboolean(SectionTypes.DEFAULT, "headless")
        return  BrowserFactory().get_browser(browser_name)


    async def close(self, browser: Browser) -> None:
        await browser.close()
