import unittest

from selenium.webdriver import ActionChains

from chapter3.po_1 import Search

from setting import*


class TestA(unittest.TestCase, Search):

    @classmethod
    def setUpClass(cls) -> None:
        ...

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.get()
        self.login()

    def tearDown(self) -> None:
        self.driver.refresh()

    def test_search_bug(self):
        self.driver.switch_to.frame('appIframe-my')
        ActionChains(self.driver).move_to_element(self.element(self.home)).perform()
        assert self.element(self.user_name).text == 'admin'
        self.driver.switch_to.default_content()
        print('test_login is ok')

    def test_logout(self):
        self.logout()
        assert self.driver.current_url == 'http://127.0.0.1/zentao/user-login.html'