import unittest
from chapter6.decorators import depend
# from chapter5.decorators import *


class TestA(unittest.TestCase):

    def test_a(self):
        print(self.test_a.__name__)
        assert True

    def test_b(self):
        print(self.test_b.__name__)
        assert 1 == 0

    @depend('test_a')
    def test_c(self):
        print(self.test_c.__name__)
        assert 1


class TestB(unittest.TestCase):
    @depend('test_a')
    def test_d(self):
        print('111')
        print(self.test_d.__name__)


if __name__ == '__main__':
    unittest.main(verbosity=2)