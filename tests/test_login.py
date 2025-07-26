import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_login_succeeds_with_valid_credentials(page):
    await page.goto("https://www.saucedemo.com/v1/")
    user_name_text_box = page.locator("#user-name")
    password_text_box = page.locator("#password")
    login_button = page.locator('//input[@value="LOGIN"]')
    await user_name_text_box.fill("standard_user")
    await password_text_box.fill("secret_sauce")
    await login_button.click()

    await expect(page.get_by_text("Products")).to_be_visible()
    await page.wait_for_timeout(5000)
