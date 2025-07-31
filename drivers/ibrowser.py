from abc import ABC, abstractmethod

from playwright.async_api import Browser, Playwright


class IBrowser(ABC):
    @abstractmethod
    async def create_browser(self,playwright: Playwright)->Browser: ...
