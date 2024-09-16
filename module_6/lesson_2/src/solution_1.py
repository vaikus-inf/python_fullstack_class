import unittest

def return_unique_numbers(list_numbers):
      unique_list_number = []
      for number in list_numbers:
          if number not in unique_list_number:
              unique_list_number.append(number)
      return unique_list_number

class TestGetUniqueNumbers(unittest.TestCase):

    def test_with_duplicates(self):
        self.assertEqual(return_unique_numbers([1, 2, 3, 4, 3, 5, 2, 3]), [1, 2, 3, 4, 5])

    def test_with_negative_numbers(self):
        self.assertEqual(return_unique_numbers([-2, 0, 3, 0, -2]), [-2, 0, 3])

    def test_without_duplicates(self):
        self.assertEqual(return_unique_numbers([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(return_unique_numbers([]), [])

if __name__ == '__main__':
    unittest.main()
