# 页面属性封装（url, 浏览器实例，元素，操作）
# 页面调用（页面继承，页面实例化）
# 基于页面调用可以有两种实现方式
from time import sleep

from selenium.webdriver import ActionChains

from chapter3.bo_demo import CHROME
from setting import *


# 页面基类，进行了基础属性封装
class Page:
    url = None
    driver = None

    @classmethod
    def cls_element(cls, loc: tuple):
        """
        类方法，定位元素的方法
        :param loc:
        :return:
        """
        return cls.driver.find_element(*loc)

    def element(self, loc: tuple):
        """
        定位元素的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)

    @classmethod
    def cls_elements(cls, loc: tuple):
        """
        类方法，定位元素组的方法或多个元素
        :param loc:
        :return:
        """
        return cls.driver.find_elements(*loc)

    def elements(self, loc: tuple):
        """
        定位元素组的方法或多个元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*loc)


# 业务页面封装：浏览器实例...（公用方法
class CommonLoginPage(Page):
    url = PROJECT_ZenTao_URL
    driver = CHROME().browser
    username = ('id', 'account')
    password = ('name', 'password')
    loginBtn = ('id', 'submit')
    logoutBtn = ('xpath', '//*[@id="userNav"]/li[1]/ul/li[14]/a')
    home = ('xpath', '//*[@id="userNav"]/li[1]/a/div')

    @classmethod
    def cls_get(cls):
        """
        类方法，打开首页地址
        :return:
        """
        cls.driver.get(cls.url)

    def get(self):
        """
        打开首页地址
        :return:
        """
        self.driver.get(self.url)

    @classmethod
    def cls_login(cls, username: str = 'admin', password: str = 'Aaa123456'):
        cls.cls_element(cls.username).send_keys(username)
        cls.cls_element(cls.password).send_keys(password)
        cls.cls_element(cls.loginBtn).click()

    def login(self, username: str = 'admin', password: str = 'Aaa123456'):
        self.element(self.username).send_keys(username)
        self.element(self.password).send_keys(password)
        self.element(self.loginBtn).click()

    @classmethod
    def cls_logout(cls):
        cls.driver.switch_to.frame('appIframe-my')
        ActionChains(cls.driver).move_to_element(cls.cls_element(cls.home)).perform()
        cls.cls_elements(cls.logoutBtn).click()

    def logout(self):
        self.driver.switch_to.frame('appIframe-my')
        ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
        self.element(self.logoutBtn).click()
        # print('test_logout is ok')


# 项目业务页面
class Search(CommonLoginPage):

    searchInput = ('id', 'globalSearchInput')
    searchBtn = ('id', 'globalSearchButton')
    user_name = ('xpath', '//*[@id="userNav"]/li[1]/ul/li[1]/a/div[2]')

    bug_label = ('xpath', '//*[@id="mainMenu"]/div[1]/div[2]/span[1]')

    def search_bug(self, bug_id: str = '001'):
        self.element(self.searchInput).send_keys(bug_id)
        self.element(self.searchBtn).click()


class TestSearch(Search):
    """
    测试登录和检索bug功能
    """
    def test_login(self):
        self.get()
        self.login()
        self.driver.switch_to.frame('appIframe-my')
        ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
        assert self.element(self.user_name).text == 'admin'
        self.driver.switch_to.default_content()
        print('test_login is ok')

    def test_search_bug(self):
        self.driver.switch_to.default_content()
        self.search_bug()
        self.driver.switch_to.frame('appIframe-qa')
        sleep(1)
        assert self.element(self.bug_label).text == '1'
        print('test_search_bug is ok')
        self.driver.switch_to.default_content()
        self.driver.quit()

    # def test_logout(self):
    #     self.driver.switch_to.frame('appIframe-my')
    #     ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
    #     self.element(self.logoutBtn).click()
    #     print('test_logout is ok')
        # self.driver.switch_to.default_content()


# obj = TestSearch()
# obj.test_login()
# obj.logout()
# obj.test_search_bug()







