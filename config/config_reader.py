import configparser
from typing import Optional

from config.iconfig_reader import IConfigReader
from constants.framework_constants import FrameworkConstants
from enums.section_types import SectionTypes


class ConfigReader(IConfigReader):
    __instance = None
    __config = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(ConfigReader, cls).__new__(cls, *args, **kwargs)
            cls.__config = configparser.RawConfigParser()
            cls.__config.read(FrameworkConstants.FRAMEWORK_CONFIG_FILE_PATH)
        return cls.__instance

    def get(self, section_type: SectionTypes, key: str) -> str:
        return self.__config.get(section_type.value, key.lower())

    def getboolean(self,section_type: SectionTypes, key: str) -> bool:
        return self.__config.getboolean(section_type.value,key)

    def getint(self,section_type: SectionTypes, key: str) -> int:
        pass

    def getfloat(self,section_type: SectionTypes, key: str) -> float:
        pass
