from abc import ABC, abstractmethod

from enums.section_types import SectionTypes


class IConfigReader(ABC):
    @abstractmethod
    def get(self, section: SectionTypes, key: str) -> str: ...

    @abstractmethod
    def getboolean(self, section: SectionTypes, key: str) -> bool: ...

    @abstractmethod
    def getint(self, section: SectionTypes, key: str) -> int: ...

    @abstractmethod
    def getfloat(self, section: SectionTypes, key: str) -> float: ...
