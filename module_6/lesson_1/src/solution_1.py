import unittest

def sum_numbers(x, y):
    return x + y

class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        result = sum_numbers(3, 4)
        self.assertEqual(result, 7)

def diff_numbers(x, y):
    return x - y

class TestDiffNumbers(unittest.TestCase):
    def test_diff_numbers(self):
        result = diff_numbers(6, 3)
        self.assertEqual(result, 3)

def abs_num(x):
    return abs(x)

class TestAbsNum(unittest.TestCase):
    def test_abs_num(self):
        result = abs_num(-5)
        self.assertEqual(result, 5)

def comp_numbers(x, y):
    return x * y

class TestCompNumbers(unittest.TestCase):
    def test_comp_numbers(self):
        result = comp_numbers(3, 4)
        self.assertEqual(result, 12)

def square_num(x):
    return x ** 0.5

class TestSquareNum(unittest.TestCase):
    def test_square_num(self):
        result = square_num(4)
        self.assertEqual(result, 2)

def div_numbers(x, y):
    if y == 0:
        raise ValueError('Деление на ноль!')
    return x / y

class TestDivNumbers(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            div_numbers(6, 0)
    
    def test_div_numbers(self):
        result = div_numbers(6, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
