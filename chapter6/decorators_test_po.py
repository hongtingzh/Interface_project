# 页面属性封装（url, 浏览器实例，元素，操作）
# 页面调用（页面继承，页面实例化）
# 基于页面调用可以有两种实现方式
import unittest
from time import sleep

from selenium.webdriver import ActionChains

from chapter5.po_1 import Search
from chapter6.decorators import depend, logs


class TestSearch(unittest.TestCase, Search):
    """
    测试登录和检索bug功能
    """
    @logs
    def test_login(self):
        self.get()
        self.login()
        self.driver.switch_to.frame('appIframe-my')
        ActionChains(self.driver).move_to_element(self.element('cp.home')).perform()
        assert self.element('sp.user_name').text == 'adminn'
        self.driver.switch_to.default_content()
        print('test_login is ok')
        sleep(1)
        self.logout()

    # @function2 ===> function2(function1) ==返回结果==> wraps_func  函数对象
    # @depend('test_login') ===> depend(test_search_bug(self))('test_login') ===> wraps_func('test_login')
    # function1() ==执行==> wraps_func()

    @logs
    @depend('test_login')
    def test_search_bug(self):
        # self.driver.switch_to.default_content()
        # sleep(1)
        # self.driver.switch_to.default_content()
        # self.get()
        print('test_login3')
        self.login()
        print('test_login4')
        self.driver.switch_to.default_content()
        self.search_bug()
        self.driver.switch_to.frame('appIframe-qa')
        sleep(1)
        assert self.element('sp.bug_label').text == '1'
        print('test_search_bug is ok')

        # self.driver.switch_to.default_content()
        # self.logout()
        # self.driver.quit()


#         depend('test_login)


if __name__ == '__main__':
    unittest.main(verbosity=2)






