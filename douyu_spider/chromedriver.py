
from selenium.webdriver.chrome.webdriver import WebDriver


class ChromeDriver(WebDriver):

    def __init__(self, user=None, pwd=None):
        self.executable_path = r'E:\Develop\spider\software\chromedriver.exe'
        self.options = WebDriver.create_options(self)
        self.options.add_argument(r"user-data-dir=C:\Users\Administrator.XSOOY-20170317P\AppData\Local\Google\Chrome\User Data")
        # self.options.set_headless()
        # extension_path = '/extension/path'
        # self.options.add_extension(extension_path)
        try:
            WebDriver.__init__(
                self,
                executable_path=self.executable_path,
                options=self.options)
        except Exception:
            self.quit()
            raise
        self.user = user
        self.pwd = pwd


# options = webdriver.FirefoxOptions()
# options.set_headless()
# options.add_argument('-headless')
# options.add_argument('--disable-gpu')
# firefoxProfile = webdriver.FirefoxProfile()
## Disable CSS
# firefoxProfile.set_preference('permissions.default.stylesheet', 2)
## Disable images
# firefoxProfile.set_preference('permissions.default.image', 2)
## Disable Flash
# firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',  'false')