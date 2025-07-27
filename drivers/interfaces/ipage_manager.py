from abc import ABC, abstractmethod

from playwright.async_api import Page, BrowserContext


class IPageManager(ABC):

    @abstractmethod
    async def create(self, context: BrowserContext) -> Page: ...

    @abstractmethod
    async def close(self, page: Page) -> None: ...
