# 页面属性封装（url, 浏览器实例，元素，操作）
# 页面调用（页面继承，页面实例化）
# 基于页面调用可以有两种实现方式
from chapter3.bo_demo import *


class Page:

    url = None
    locators = {}
    browser = CHROME

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browser

    def __getattr__(self, loc):
        if loc not in self.locators.keys():
            raise Exception

        by, val = self.locators[loc]
        return self.driver.find_element(by, val)


class CommonMainPage(Page):

    url = 'http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
    locators = {
        'username': ('id', 'account'),
        'password': ('name', 'password'),
        'loginBtn': ('id', 'submit')
    }

    def get(self):
        """
        打开首页地址
        :return:
        """
        self.driver.get(self.url)

    def login(self, username: str = 'admin', password: str = 'Aaa123456'):

        self.username.send_keys(username)
        self.password.send_keys(password)
        self.loginBtn.click()


class MainPage(CommonMainPage):
    CommonMainPage.locators.update({
        'searchInput': ('id', 'globalSearchInput'),
        'searchBtn': ('id', 'globalSearchButton'),
        'home': ('xpath', '//*[@id="userNav"]/li[1]/a/div'),
        'user_name': ('xpath', '//*[@id="userNav"]/li[1]/ul/li[1]/a/div[2]'),
        'bug_label': ('xpath', '//*[@id="mainMenu"]/div[1]/div[2]/span[1]')
    })

    def search_bug(self, bug_id: str = '1'):
        self.searchInput.send_keys(bug_id)
        self.searchBtn.click()
        self.driver.switch_to.frame('appIframe-qa')


class TestMain:

    def test_login(self):
        page = MainPage()
        page.get()
        page.login()
        page.driver.switch_to.frame('appIframe-my')
        ActionChains(page.driver).move_to_element(page.home).perform()
        assert page.user_name.text == 'admin'
        print('test_login is ok')
        page.driver.quit()

    def test_search_bug(self):
        page = MainPage()
        page.get()
        page.login()
        page.search_bug()
        page.driver.switch_to.frame('appIframe-qa')
        assert page.bug_label.text == '1'
        print('test_search_bug is ok')
        page.driver.quit()


# obj = TestMain()
# obj.test_login()
# obj.test_search_bug()

