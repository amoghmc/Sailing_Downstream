import unittest
from sailing_downstream_challenge import check_multiple_of_10, remove_multiples

class Unit_Test_Sailing_Downstream(unittest.TestCase):

    def test_check_multiple_of_10(self):
        result = check_multiple_of_10([])
        self.assertEqual(result, True)
        result = check_multiple_of_10([1, 2, 3])
        self.assertEqual(result, False)
        result = check_multiple_of_10([i for i in range(10)])
        self.assertEqual(result, True)
        result = check_multiple_of_10([i for i in range(20)])
        self.assertEqual(result, True)
        result = check_multiple_of_10([i for i in range(21)])
        self.assertEqual(result, False)

    def test_remove_multiples(self):
        result = remove_multiples([1, 2, 3])
        self.assertEqual(result, [1])
        result = remove_multiples([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(result, [1, 5, 7])
        result = remove_multiples([])
        self.assertEqual(result, [])
        result = remove_multiples([1])
        self.assertEqual(result, [1])


if __name__ == '__main__':
    unittest.main()
