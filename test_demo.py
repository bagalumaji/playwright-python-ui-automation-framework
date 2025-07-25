import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_demo():
    pw = await async_playwright().start()
    browser = await pw.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.google.com")
    await page.close()
    await context.close()
    await browser.close()
    await pw.stop()
