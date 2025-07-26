import pytest_asyncio
from playwright.async_api import Playwright, Browser, BrowserContext

from drivers.browser_context_manager import BrowserContextManager
from drivers.browser_manager import BrowserManager
from drivers.page_driver import PageDriver
from drivers.playwright_manager import PlaywrightManager


@pytest_asyncio.fixture
async def playwright():
    playwright_manager = PlaywrightManager()
    pw = await playwright_manager.start_playwright()
    yield pw
    await playwright_manager.stop_playwright(pw)


@pytest_asyncio.fixture
async def browser(playwright: Playwright):
    browser_manager = BrowserManager()
    browser = await browser_manager.launch_browser(playwright)
    yield browser
    await browser_manager.close_browser(browser)


@pytest_asyncio.fixture
async def browser_context(browser: Browser):
    browser_context_manager = BrowserContextManager()
    browser_context = await browser_context_manager.create_browser_context(browser)
    yield browser
    await browser_context_manager.close_browser_context(browser_context)


@pytest_asyncio.fixture
async def page(browser_context: BrowserContext):
    page_driver = PageDriver()
    new_page = await page_driver.new_page(browser_context)
    yield new_page
    await page_driver.close_driver(new_page)
