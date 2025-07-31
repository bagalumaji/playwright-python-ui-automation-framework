from abc import ABC, abstractmethod

from playwright.async_api import Browser

from drivers.ibrowser import IBrowser


class IBrowserManager(ABC):

    @abstractmethod
    async def launch(self) -> IBrowser: ...

    @abstractmethod
    async def close(self, browser: Browser) -> None: ...
