import unittest
from time import sleep

from selenium.webdriver import ActionChains

from chapter3.po_1 import Search
import paramunittest


# 参数化方法一：通过第三方包paramunittest
# @paramunittest.parametrized(('admin', 'Aaa123456', 'admin', 'adm test_login is ok'),
#                             ('Hongting001', 'Aaa123456', 'Hongting001', 'Hongting001 test_login is ok'),
#                             ('Hongting002', 'Aaa123456', 'Hongting002', 'Hongting002 test_login is ok'))
# class TestSearch(unittest.TestCase, Search):
#     def setParameters(self, name, pwd, ass, txt):
#         self.name = name
#         self.pwd = pwd
#         self.ass = ass
#         self.txt = txt
#
#     def test_login(self):
#         self.get()
#         self.login(self.name, self.pwd)
#         sleep(1)
#         self.driver.switch_to.frame('appIframe-my')
#         ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
#         sleep(1)
#         assert self.element(self.user_name).text == self.ass
#         print(self.txt)
#         self.driver.switch_to.default_content()
#         self.logout()

    # def test_login_admin(self):
    #     self.get()
    #     self.login('admin', 'Aaa123456')
    #     self.driver.switch_to.frame('appIframe-my')
    #     ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
    #     assert self.element(self.user_name).text == 'admin'
    #     print('adm test_login is ok')
    #     self.driver.switch_to.default_content()
    #     self.logout()
    #
    # def test_login_hongting001(self):
    #     self.get()
    #     self.login('Hongting001', 'Aaa123456')
    #     self.driver.switch_to.frame('appIframe-my')
    #     ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
    #     assert self.element(self.user_name).text == 'Hongting001'
    #     print('Hongting001 test_login is ok')
    #     self.driver.switch_to.default_content()
    #     self.logout()
    #
    # def test_login_hongting002(self):
    #     self.get()
    #     self.login('Hongting002', 'Aaa123456')
    #     self.driver.switch_to.frame('appIframe-my')
    #     ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
    #     assert self.element(self.user_name).text == 'Hongting002'
    #     print('Hongting002 test_login is ok')
    #     self.driver.switch_to.default_content()
    #     self.logout()
    #     self.driver.quit()


# 参数化方法二：使用unittest内置的subTest()
data = ({'name': 'admin', 'pwd': 'Aaa123456', 'ass': 'admin', 'txt': 'adm test_login is ok'},
        {'name': 'Hongting001', 'pwd': 'Aaa123456', 'ass': 'Hongting001', 'txt': 'Hongting001 test_login is ok'},
        {'name': 'Hongting002', 'pwd': 'Aaa123456', 'ass': 'Hongting', 'txt': 'Hongting002 test_login is ok'})


class A(unittest.TestCase, Search):
    def test_login(self):
        for d in data:
            with self.subTest(d):
                self.get()
                self.login(d['name'], d['pwd'])
                sleep(1)
                self.driver.switch_to.frame('appIframe-my')
                ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
                sleep(1)
                # assert self.element(self.user_name).text == d['ass']    # 最开始的断言方法

                # assert self.element(self.user_name).text == d['ass'], \
                #     self.driver.save_screenshot(f'./{d["ass"]}.png')    # unittest断言方法一，断言失败则截图

                try:
                    self.assertEqual(self.element(self.user_name).text, d['ass'])
                except AssertionError:
                    self.driver.save_screenshot(f'./{d["ass"]}.png')
                    raise AssertionError

                print(d['txt'])
                self.driver.switch_to.default_content()
                self.logout()


if __name__ == '__main__':
    unittest.main()
