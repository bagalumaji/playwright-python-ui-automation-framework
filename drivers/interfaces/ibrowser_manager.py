from abc import ABC, abstractmethod

from playwright.async_api import Playwright, Browser


class IBrowserManager(ABC):

    @abstractmethod
    async def launch(self, playwright: Playwright) -> Browser: ...

    @abstractmethod
    async def close(self, browser: Browser) -> None: ...
