import unittest
from time import sleep

from selenium.webdriver import ActionChains

from chapter3.po_1 import Search


class TestB(unittest.TestCase, Search):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_get()
        cls.cls_login()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    def test_search_bug(self):
        self.login()
        self.driver.switch_to.default_content()
        self.search_bug()
        self.driver.switch_to.frame('appIframe-qa')
        sleep(1)
        assert self.element(self.bug_label).text == '1'
        print('test_search_bug is ok')
        self.driver.switch_to.default_content()

    def test_logout(self):
        self.logout()
        assert self.driver.current_url == 'http://127.0.0.1/zentao/user-login.html'
        print('test_logout is ok')
