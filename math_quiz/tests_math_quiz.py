import unittest
from math_quiz import generate_random_integer, generate_operator, perform_arithmetic_operation

class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
        print("Random integer generator function is successful")

    def test_generate_operator(self):
        # Test the return value of generate_operator
        operators = {'+', '-', '*'}
        result = generate_operator()
        self.assertTrue(result in operators)
        print("Random operator generator function is successful")

    def test_perform_arithmetic_operation(self):
        # Test perform_arithmetic_operation with multiple test cases
        test_cases = [(5, 2, '+', '5 + 2', 7), (10, 5, '*', '10 * 5', 50), (8, 3, '-', '8 - 3', 5)]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_arithmetic_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)
        print("Arithmetic operation performing function is successful")

if __name__ == "__main__":
    unittest.main()
