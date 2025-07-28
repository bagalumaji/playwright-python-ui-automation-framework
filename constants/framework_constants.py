import os


class FrameworkConstants:
    __SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    __PROJECT_ROOT = os.path.abspath(os.path.join(__SCRIPT_DIR, os.pardir))
    __CONFIG_DIR = os.path.join(__PROJECT_ROOT, "resources", "config")

    FRAMEWORK_CONFIG_FILE_PATH = os.path.join(__CONFIG_DIR, "config.ini")
