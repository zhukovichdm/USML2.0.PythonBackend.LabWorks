from gcd import gcd
import unittest


class MyTest(unittest.TestCase):
    def test_zero(self):
        with self.subTest():
            self.assertEqual(gcd(0, 0), 0)

    def test_positive(self):
        d = {'param a': (3, 2, 7, 14, 0, 5),
             'param b': (6, 6, 5, 21, 5, 0),
             'result': (3, 2, 1,  7, 5, 5)}
        _len = len(d.get('param a'))

        for i in range(_len):
            a = d.get('param a')[i]
            b = d.get('param b')[i]
            r = d.get('result')[i]

            with self.subTest('param a = %d, param b = %d, Expected Result = %d' % (a, b, r)):
                self.assertEqual(gcd(a, b), r, msg='Result != Expected Result')

    def test_negative(self):
        d = {'param a': (-14, -4, 3, -4),
             'param b': (21, 3, -4, 4),
             'result': (7, -1, -1, 4)}
        _len = len(d.get('param a'))

        for i in range(_len):
            a = d.get('param a')[i]
            b = d.get('param b')[i]
            r = d.get('result')[i]

            with self.subTest('param a = %d, param b = %d, Expected Result = %d' % (a, b, r)):
                self.assertEqual(gcd(a, b), r, msg='Result != Expected Result')


class ExceptionTest(unittest.TestCase):
    def test_exception(self):
        d = {'param a': (3, 2, 7, 14, -14, -4, 3, -4, 0, 5, "qwe"),
             'param b': (6, 6, 5, 21, 21, 3, -4, 4, 5, 0, "abc")}
        _len = len(d.get('param a'))

        for i in range(_len):
            a = d.get('param a')[i]
            b = d.get('param b')[i]

            with self.subTest('param a = %d, param b = %d' % (a, b)):
                self.assertRaises(ValueError, gcd, a, b)


if __name__ == '__main__':
    unittest.main()
