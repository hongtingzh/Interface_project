import unittest


class A(unittest.TestCase):
    def test_a(self):
        assert (_length := self.test_a.__name__.__len__() == 4), \
            print(f'test_a方法名称：{_length} != 4')

    def test_b(self):
        try:
            self.assertEqual(_length := self.test_b.__name__.__len__(), 4)
        except AssertionError:
            print(f'test_b方法名称：{_length} != 4')
            raise AssertionError(f'test_b方法名称：{_length} != 4')


