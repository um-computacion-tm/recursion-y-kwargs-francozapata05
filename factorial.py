import unittest

def factorial(n):

    if n == 1:
        return 1

    else:
        return n * factorial(n-1)

class TestFactorial(unittest.TestCase):
    def test_1(self):
        resultado = factorial(1)
        self.assertEqual(resultado,1)

    def test_2(self):
        resultado = factorial(2)
        self.assertEqual(resultado,2)
    
    def test_3(self):
        resultado = factorial(3)
        self.assertEqual(resultado,6)

    def test_4(self):
        resultado = factorial(4)
        self.assertEqual(resultado,24)

    def test_6(self):
        resultado = factorial(6)
        self.assertEqual(resultado,720)

    def test_10(self):
        resultado = factorial(10)
        self.assertEqual(resultado,3628800)

unittest.main()
