import unittest
from unittest.mock import patch
from io import StringIO
from sailing_downstream_challenge import (check_multiple_of_10,
										  remove_multiples,
										  get_input)


class Unit_Test_Sailing_Downstream(unittest.TestCase):

	# test with invalid input of letters
	@patch('builtins.input', return_value='a b c d')
	@patch('sys.stdout', new_callable=StringIO)
	def test_process_input_letters(self, mock_stdout, mock_input):
		result = get_input()

		# Assertions
		mock_input.assert_called_once_with("Enter a list of integers separated by space\n")
		self.assertEqual(result, None)

	# test with invalid input of ints separated by commas
	@patch('builtins.input', return_value='1, 2, 3, 4')
	@patch('sys.stdout', new_callable=StringIO)
	def test_process_input(self, mock_stdout, mock_input):
		result = get_input()

		# Assertions
		mock_input.assert_called_once_with("Enter a list of integers separated by space\n")
		self.assertEqual(result, None)

	# test with valid input
	@patch('builtins.input', return_value='1 2 3 4')
	@patch('sys.stdout', new_callable=StringIO)
	def test_process_input(self, mock_stdout, mock_input):
		result = get_input()
		printed_output = mock_stdout.getvalue().strip()

		# Assertions
		mock_input.assert_called_once_with("Enter a list of integers separated by space\n")
		self.assertEqual(result, [1, 2, 3, 4])
		self.assertEqual(printed_output, '')

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
