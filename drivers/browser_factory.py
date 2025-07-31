from drivers.browsers.chrome_browser import ChromeBrowser
from drivers.browsers.chromium_browser import ChromiumBrowser
from drivers.browsers.edge_browser import EdgeBrowser
from drivers.browsers.firefox_browser import FirefoxBrowser
from drivers.browsers.webkit_browser import WebkitBrowser
from drivers.ibrowser import IBrowser


class BrowserFactory:
    def __init__(self):
        self.browser_mapping = {
            "chrome": lambda :ChromeBrowser(),
            "edge": lambda: EdgeBrowser(),
            "firefox": lambda: FirefoxBrowser(),
            "webkit":  lambda:WebkitBrowser(),
        }

    def get_browser(self, browser_name: str) -> IBrowser:
        browser_cls = self.browser_mapping.get(browser_name,  lambda: ChromiumBrowser())
        return browser_cls()
