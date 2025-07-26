import pytest
from playwright.async_api import expect

from pages.login_page import LoginPage


@pytest.mark.asyncio
async def test_login_succeeds_with_valid_credentials(page):
    username="standard_user"
    password="secret_sauce"

    await page.goto("https://www.saucedemo.com/v1/")
    login_page = LoginPage(page)
    await login_page.login_to_application(username, password)
    await expect(page.get_by_text("Products")).to_be_visible()
    await page.wait_for_timeout(5000)
