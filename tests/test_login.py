import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.asyncio
async def test_login_succeeds_with_valid_credentials(page):
    username="standard_user"
    password="secret_sauce"

    await page.goto("https://www.saucedemo.com/v1/")
    login_page = LoginPage(page)
    await login_page.login_to_application(username, password)

    product_page = ProductPage(page)
    await product_page.verify_product_title_is_displayed()

    await page.wait_for_timeout(5000)
