import pytest


@pytest.mark.asyncio
async def test_demo(page):
    await page.goto("https://www.google.com")
