import unittest
from unittest import skip, skipIf, skipUnless


@skip
class A(unittest.TestCase):

    def test_a1(self):
        self.assertEqual(1, 2)

    def test_a2(self):
        ...


@skipIf(1 == 2, '')
class B(unittest.TestCase):

    @skipIf(2 == 2, '')
    def test_b1(self):
        ...

    @skipUnless(3 > 2, '')
    def test_b2(self):
        ...
