from typing import Any, AsyncGenerator

import pytest_asyncio
from playwright.async_api import Playwright, Browser, BrowserContext, Page

from drivers.browser_context_manager import BrowserContextManager
from drivers.browser_manager import BrowserManager
from drivers.page_driver import PageDriver
from drivers.playwright_manager import PlaywrightManager


@pytest_asyncio.fixture
async def playwright()-> AsyncGenerator[Playwright, Any]:
    manager = PlaywrightManager()
    pw = await manager.start()
    yield pw
    await manager.stop(pw)


@pytest_asyncio.fixture
async def browser(playwright: Playwright)-> AsyncGenerator[Browser, Any]:
    manager = BrowserManager()
    browser = await manager.launch(playwright)
    yield browser
    await manager.close(browser)


@pytest_asyncio.fixture
async def browser_context(browser: Browser)-> AsyncGenerator[BrowserContext, Any]:
    manager = BrowserContextManager()
    browser_context = await manager.create(browser)
    yield browser_context
    await manager.close(browser_context)


@pytest_asyncio.fixture
async def page(browser_context: BrowserContext)-> AsyncGenerator[Page, Any]:
    driver = PageDriver()
    new_page = await driver.create(browser_context)
    yield new_page
    await driver.close(new_page)
