from abc import ABC, abstractmethod


class IBrowserManager(ABC):

    @abstractmethod
    async def launch(self): ...

    @abstractmethod
    async def close(self): ...
