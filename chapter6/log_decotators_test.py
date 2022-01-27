from chapter6.decorators import logs
import unittest


@logs
def func_a(*args, **kwargs):
    return 1 / args.__len__(), 1 / kwargs.__len__()


# func_a(1, name='json')
func_a()
# class TestA(unittest.TestCase):
#
#     @logs
#     def test_a(self):
#         assert False
#
#     @logs
#     def test_b(self):
#         assert True
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)