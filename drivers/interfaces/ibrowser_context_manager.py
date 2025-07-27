from abc import ABC, abstractmethod

from playwright.async_api import Browser, BrowserContext


class IBrowserContextManager(ABC):

    @abstractmethod
    async def create(self, browser: Browser) -> BrowserContext: ...

    @abstractmethod
    async def close(self, context: BrowserContext) -> None: ...
