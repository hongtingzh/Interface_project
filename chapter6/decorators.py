from functools import wraps
import unittest
from chapter6.logs import log


class DependencyError(Exception):

    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        if self._type == 0:
            return f'Dependency name of test is required!'
        if self._type == 1:
            return f'Dependency name of test not the case self!'


def depend(case=''):
    if not case:
        raise DependencyError
    _mark = []

    def inner_func(func):
        @wraps(func)
        def wraps_func(self):
            if case == func.__name__:
                raise DependencyError(1)
            _r = self._outcome.result
            _f, _e, _s = _r.failures, _r.errors, _r.skipped

            if not (_f or _e or _s):
                f = func(self)
                return f

            if _f:
                _mark.extend([fail[0] for fail in _f])
            if _e:
                _mark.extend([error[0] for error in _e])
            if _s:
                _mark.extend([skip[0] for skip in _s])
            f = unittest.skipIf(
                case in str(_mark),
                f'The pre-depend case:{case} has failed! Skip the specified case!'
            )(func)(self)
            return f
        return wraps_func
    return inner_func

# depend('test_login')(test_search_bug)
# inner_func(test_search_bug)
# wraps_func


def logs(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        tuple_args = args
        dict_kwargs = kwargs
        try:
            func(*args, **kwargs)
            log.debug(
                f'{func.__name__}(*args: tuplr = *{tuple_args}), **kwargs: dict = **{dict_kwargs}',
                extra={'status': 'PASS'}
            )
        except Exception:
            log.exception(
                f'{func.__name__}(*args: tuplr = *{tuple_args}), **kwargs: dict = **{dict_kwargs}',
                exc_info=True,  # 是否记录异常的信息
                extra={'status': 'FAIL'}
            )
            raise   # 得将失败结果抛出，要不然测试用例会断言错误也会执行成功
    return wrap_func
