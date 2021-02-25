import fibo
import unittest

class TestFibonacciFunctions(unittest.TestCase):

    def test_series_100(self):
        print('\nTest Series 100')
        wanted_result = [0,1,1,2,3,5,8,13,21,34,55,89]
        test_result = fibo.fib(100)
        self.assertEqual(wanted_result,test_result)

    def test_series_50(self):
        print('\nTest Series 50')
        wanted_result = [0,1,1,2,3,5,8,13,21,34]
        test_result = fibo.fib(50)
        self.assertEqual(wanted_result,test_result)

if __name__ == '__main__' : unittest.main()
