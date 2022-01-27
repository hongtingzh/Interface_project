from chapter6.decorators import logs
# from chapter6.logs import log
import unittest


@logs
def func_a(*args, **kwargs):
    # log.debug(func_a.__name__, extra={'status': 'running'})

    return 1 / args.__len__(), 1 / kwargs.__len__()


# func_a(1, name='json')
func_a()


# class TestA(unittest.TestCase):
#
#     @logs
#     def test_a(self):
#         # log.debug(self.test_a.__name__, extra={'status': 'running'})
#         assert True
#
#     @logs
#     def test_b(self):
#         # log.debug(self.test_b.__name__, extra={'status': 'running'})
#         assert True
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)