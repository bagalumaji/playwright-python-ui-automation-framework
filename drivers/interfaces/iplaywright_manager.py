from abc import ABC, abstractmethod

from playwright.async_api import Playwright


class IPlaywrightManager(ABC):
    @abstractmethod
    async def start(self) -> Playwright: ...

    @abstractmethod
    async def stop(self, playwright: Playwright) -> None: ...
