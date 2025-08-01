from playwright.async_api import Page, Locator, expect

from uiactions.assertions import Assertions


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def __product_title_locator(self) -> Locator:
        return self.page.get_by_text("Products")

    async def verify_product_title_is_displayed(self) -> None:
        await Assertions.is_visible(self.__product_title_locator)
