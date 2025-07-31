from typing import Any, AsyncGenerator

import pytest_asyncio
from playwright.async_api import Playwright, Browser, BrowserContext, Page

from drivers.browser_context_manager import BrowserContextManager
from drivers.browser_manager import BrowserManager
from drivers.ibrowser import IBrowser
from drivers.interfaces.ibrowser_context_manager import IBrowserContextManager
from drivers.interfaces.ibrowser_manager import IBrowserManager
from drivers.interfaces.ipage_manager import IPageManager
from drivers.interfaces.iplaywright_manager import IPlaywrightManager
from drivers.page_manager import PageManager
from drivers.playwright_manager import PlaywrightManager


@pytest_asyncio.fixture
async def playwright() -> AsyncGenerator[Playwright, Any]:
    manager: IPlaywrightManager = PlaywrightManager()
    pw = await manager.start()
    yield pw
    await manager.stop(pw)


@pytest_asyncio.fixture
async def launched_browser(playwright: Playwright) -> AsyncGenerator[Browser, Any]:
    manager: IBrowserManager = BrowserManager()
    i_browser:IBrowser = await manager.launch()
    browser = await i_browser.create_browser(playwright)
    yield browser
    await manager.close(browser)


@pytest_asyncio.fixture
async def test_context(launched_browser: Browser) -> AsyncGenerator[BrowserContext, Any]:
    manager: IBrowserContextManager = BrowserContextManager()
    browser_context = await manager.create(launched_browser)
    yield browser_context
    await manager.close(browser_context)


@pytest_asyncio.fixture
async def page(test_context: BrowserContext) -> AsyncGenerator[Page, Any]:
    driver: IPageManager = PageManager()
    new_page = await driver.create(test_context)
    yield new_page
    await driver.close(new_page)
