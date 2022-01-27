# 继承测试
# 测试类应该是被测页面的子类

# 实例测试
# 测试类应该是获得被测页面的实例

import unittest
from time import sleep

from chapter3.po_demo2 import MainPage


class A(unittest.TestCase):

    def setUp(self) -> None:
        self.page = MainPage()
        self.page.get()
        self.page.login()

    def test_a(self):
        self.page.search_bug()
        assert self.page.bug_label.text == '1'

    def tearDown(self) -> None:
        self.page.driver.quit()
