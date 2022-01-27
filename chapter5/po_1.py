# 页面属性封装（url, 浏览器实例，元素，操作）
# 页面调用（页面继承，页面实例化）
# 基于页面调用可以有两种实现方式
from time import sleep

from selenium.webdriver import ActionChains

from chapter3.bo_demo import CHROME
from chapter5.file_reader import YamlReader
from setting import *


# 页面基类，进行了基础属性封装
class Page:
    url = None
    driver = None

    # 子类重写，获取通用配置文件中具体项目的元素配置文件字典
    # elements_yml = None
    elements_yml = {}

    # 缓存动态读取
    elements_pool = {}

    def _locator(self, expression: str = 'cp.username'):
        """
        解析元素表达式的方法
        :param expression:
        :return:
        """
        name, value = expression.split('.')
        if name not in self.elements_yml:
            raise Exception('元素配置文件的路径：{}无法识别'.format(name))
        if name not in self.elements_pool:
            self.elements_pool[name] = YamlReader(self.elements_yml[name]).data
            if (locator := self.elements_pool[name][value])[0] not in BY_RULES:
                raise Exception(
                    f'无法识别定位方法：{locator}'
                )
            return locator
        return self.elements_pool[name][value]

    @classmethod
    def cls_locator(cls, expression: str = 'cp.username'):
        """
        解析元素表达式的方法
        :param expression:
        :return:
        """
        name, value = expression.split('.')
        if name not in cls.elements:
            raise Exception('元素配置文件的路径：{}无法识别'.format(name))
        if name not in cls.elements_pool:
            cls.elements_pool[name] = YamlReader(cls.elements_yml[name]).data
            if (locator := cls.elements_pool[name][value])[0] not in BY_RULES:
                raise Exception(
                    f'无法识别定位方法：{locator}'
                )
            return locator
        return cls.elements_pool[name][value]

    @classmethod
    def cls_element(cls, loc: str):
        """
        类方法，定位元素的方法
        :param loc:
        :return:
        """
        return cls.driver.find_element(*cls.cls_locator(loc))

    def element(self, loc: str):
        """
        定位元素的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*self._locator(loc))

    @classmethod
    def cls_elements(cls, loc: str):
        """
        类方法，定位元素组的方法或多个元素
        :param loc:
        :return:
        """
        return cls.driver.find_elements(*cls.cls_locator(loc))

    def elements(self, loc: str):
        """
        定位元素组的方法或多个元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*self._locator(loc))


# 业务页面封装：浏览器实例...（公用方法
class CommonLoginPage(Page):
    url = PROJECT_ZenTao_URL
    driver = CHROME().browser
    # username = ('id', 'account')
    # password = ('name', 'password')
    # loginBtn = ('id', 'submit')
    # logoutBtn = ('xpath', '//*[@id="userNav"]/li[1]/ul/li[14]/a')
    # home = ('xpath', '//*[@id="userNav"]/li[1]/a/div')
    elements_yml = YAML_ELEMENT

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
        cls.cls_element('cp.username').send_keys(username)
        cls.cls_element('cp.password').send_keys(password)
        cls.cls_element('cp.loginBtn').click()

    def login(self, username: str = 'admin', password: str = 'Aaa123456'):
        self.element('cp.username').send_keys(username)
        self.element('cp.password').send_keys(password)
        self.element('cp.loginBtn').click()

    @classmethod
    def cls_logout(cls):
        cls.driver.switch_to.frame('appIframe-my')
        ActionChains(cls.driver).move_to_element(cls.cls_element('cp.home')).perform()
        cls.cls_elements('cp.logoutBtn').click()

    def logout(self):
        self.driver.switch_to.frame('appIframe-my')
        ActionChains(self.driver).move_to_element(self.element('cp.home')).perform()
        self.element('cp.logoutBtn').click()
        # print('test_logout is ok')


# 项目业务页面
class Search(CommonLoginPage):

    # searchInput = ('id', 'globalSearchInput')
    # searchBtn = ('id', 'globalSearchButton')
    # user_name = ('xpath', '//*[@id="userNav"]/li[1]/ul/li[1]/a/div[2]')
    #
    # bug_label = ('xpath', '//*[@id="mainMenu"]/div[1]/div[2]/span[1]')

    def search_bug(self, bug_id: str = '001'):
        self.element('sp.searchInput').send_keys(bug_id)
        self.element('sp.searchBtn').click()


class TestSearch(Search):
    """
    测试登录和检索bug功能
    """
    def test_login(self):
        self.get()
        self.login()
        self.driver.switch_to.frame('appIframe-my')
        ActionChains(self.driver).move_to_element(self.element('cp.home')).perform()
        assert self.element('sp.user_name').text == 'admin'
        self.driver.switch_to.default_content()
        print('test_login is ok')

    def test_search_bug(self):
        # self.driver.switch_to.default_content()
        self.login()
        self.search_bug()
        self.driver.switch_to.frame('appIframe-qa')
        sleep(1)
        assert self.element('sp.bug_label').text == '1'
        print('test_search_bug is ok')
        self.driver.switch_to.default_content()
        self.driver.quit()

    # def test_logout(self):
    #     self.driver.switch_to.frame('appIframe-my')
    #     ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
    #     self.element(self.logoutBtn).click()
    #     print('test_logout is ok')
        # self.driver.switch_to.default_content()

# #
# obj = TestSearch()
# obj.test_login()
# obj.logout()
# obj.test_search_bug()







