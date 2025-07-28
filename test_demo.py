from config.config_reader import ConfigReader
from enums.section_types import SectionTypes

config = ConfigReader()
print("id : ", id(config))
headless = config.get(SectionTypes.DEFAULT, "headless")
print("------------------")
print("headless : ", headless)

config1 = ConfigReader()
print("id1 : ", id(config1))
print("headless : ",config1.get(SectionTypes.DEFAULT,"headless"))
