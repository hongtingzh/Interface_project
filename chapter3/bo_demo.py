# 浏览器类型（chrome ie firefox edge opera）
# 浏览器的启动参数（无头化，最大化，尺寸化）
# 浏览器的属性（显示尺寸， 隐式等待/页面加载/js执行时间）
from time import sleep
from typing import Type, Union
from selenium.webdriver import *
from setting import *


class BrowserTypeError(Exception):

    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'susupported browsertype: {self._type}'


class BROWSER:

    CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
    FIREFOX_DRIVER_PATH = FIREFOX_DRIVER_PATH
    IE_DRIVER_PATH = IE_DRIVER_PATH
    EDGE_DRIVER_PATH = EDGE_DRIVER_PATH
    OPERA_DRIVER_PATH = OPERA_DRIVER_PATH

    # 浏览器尺寸
    WINDOWS_SIZE = (1024, 768)
    # 隐式等待时间
    IMP_TIME = 30
    # 页面加载时间
    PAGE_LOAD_TIME = 20
    # js执行时间
    SCRIPT_TIME_OUT = 20
    # 无头化
    HEADLESS = True

    def __init__(self, browser_type: Type[Union[Chrome, Firefox, Ie, Edge, Opera]] = Chrome,
                 option_type: Type[Union[ChromeOptions, FirefoxOptions, IeOptions, EdgeOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH):
        if not issubclass(browser_type, (Chrome, Firefox, Ie, Edge, Opera)):
            # raise BrowserTypeError(browser_type)
            raise TypeError
        if not issubclass(option_type, (ChromeOptions, FirefoxOptions, IeOptions, EdgeOptions)):
            # raise BrowserTypeError(option_type)
            raise TypeError
        if not isinstance(driver_path, str):
            raise TypeError
        self._driver = browser_type
        self._path = driver_path
        self._option = option_type

    @property
    def options(self):
        """
        浏览器特定操作，在子类中实现
        :return:
        """
        return

    @property
    def browser(self):
        """
        启动浏览器，返回浏览器实例
        :return:
        """
        return


class CHROME(BROWSER):

    OPTION_MARK = CHROME_OPTION_MARK

    METHOD_MARK = CHROME_METHOD_MARK

    HEADLESS = CHROME_HEADLESS    # chrome不需要无头化启动

    IMP_TIME = CHROME_IMP_TIME

    PAGE_LOAD_TIME = CHROME_PAGE_LOAD_TIME

    SCRIPT_TIME_OUT = CHROME_SCRIPT_TIME_OUT

    WINDOWS_SIZE = CHROME_WINDOWS_SIZE

    START_MAX = CHROME_START_MAX  # 对应的是option的启动参数

    PRE = CHROME_PRE

    # 对应的option属性方法
    # EXP = {
    #     'excludeSwitches': ['enable-automation'],     # 不会提示‘正受到自动测试软件的控制’
    #     # 'credentials_enable_service': [False],
    #     # 'profile.password_manager_enabled': [False],
    #     # 'mobileEmulation': {'deviceName': 'iPhone 6'}   # 以移动模拟的形式打开某个网页，一般web用不到，在做H5需要在网页实现的时候就必须要添加
    # }
    EXP = CHROME_EXPERIMENTAL

    @property
    def options(self):      # 启动时设定
        chrome_option = self._option()
        if self.OPTION_MARK:
            chrome_option.add_argument(self.START_MAX)
            for k, v in self.EXP.items():
                chrome_option.add_experimental_option(k, v)
            # for i, j in self.PRE.items():
            #     chrome_option.add_experimental_option(i, j)
            chrome_option.add_experimental_option('prefs', self.PRE)
            chrome_option.headless = self.HEADLESS
            return chrome_option
        return None

    @property
    def browser(self):      # 启动后设定
        if self.OPTION_MARK:
            chrome = self._driver(self._path, options=self.options)
        else:
            chrome = self._driver(self._path)
        if self.METHOD_MARK:
            chrome.implicitly_wait(self.IMP_TIME)
            chrome.set_script_timeout(self.SCRIPT_TIME_OUT)
            chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
            # chrome.set_window_size(*self.WINDOWS_SIZE)
            return chrome
        return chrome


class EDGE(BROWSER):

    def __init__(self):
        super(EDGE, self).__init__(
            browser_type=Edge,
            option_type=EdgeOptions,
            driver_path=super().EDGE_DRIVER_PATH
        )

    @property
    def options(self):
        ie_option = self._option()
        return ie_option

    @property
    def browser(self):
        edge = self._driver(self._path, options=self.options)
        edge.set_script_timeout(self.SCRIPT_TIME_OUT)
        edge.set_page_load_timeout(self.PAGE_LOAD_TIME)
        edge.maximize_window()
        return edge


# with CHROME().browser as _chrome:
#     _chrome.get(PROJECT_ZenTao_URL)
#     sleep(3)

# with EDGE().browser as _edge:
#     _edge.get(PROJECT_ZenTao_URL)
#     sleep(3)


