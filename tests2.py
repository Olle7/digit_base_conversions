import unittest
from digit_base_conversions import first_numbers_in_base,number_to_list_of_digits,list_of_digits_to_number,get_digit


class TestPositionalNumeralSystemFunctions(unittest.TestCase):

    def test_test_1(self):
        self.assertEqual(1,2)


    def test_first_numbers_in_base_basic(self):
        # Test binary numbers (least significant digit first, default)
        self.assertEqual(list(first_numbers_in_base(5,2)),[[0],[1],[0,1],[1,1],[0,0,1]])

        # Test ternary numbers (least significant digit first, default)
        self.assertEqual(list(first_numbers_in_base(5,3)),[[0],[1],[2],[0,1],[1,1]])

    def test_first_numbers_in_base_most_significant_digit_first(self):
        # Test binary numbers (most significant digit first)
        self.assertEqual(list(first_numbers_in_base(5,2,most_signicant_digit_first=True)),[[0],[1],[1,0],[1,1],[1,0,0]])

        # Test ternary numbers (most significant digit first)
        self.assertEqual(list(first_numbers_in_base(5,3,most_signicant_digit_first=True)),[[0],[1],[2],[1,0],[1,1]])

    def test_number_to_list_of_digits_basic(self):
        # Convert 6 to base 2
        self.assertEqual(number_to_list_of_digits(6,2),[0,1,1])  # least significant digit first

        # Convert 6 to base 2, most significant digit first
        self.assertEqual(number_to_list_of_digits(6,2,most_signicant_digit_first=True),[1,1,0])

    def test_list_of_digits_to_number_basic(self):
        # Convert list of digits [0, 1, 1] in base 2 back to number (least significant digit first)
        self.assertEqual(list_of_digits_to_number([0,1,1],2),6)

        # Convert list of digits [1, 1, 0] in base 2 back to number (most significant digit first)
        self.assertEqual(list_of_digits_to_number([1,1,0],2,most_signicant_digit_first=True),6)

    def test_get_digit_basic(self):
        # Get the digit at position 2 in the base-2 representation of 6 (least significant digit first)
        self.assertEqual(get_digit(6,2,2),1)  # 110 (binary)

        # Get the digit at position 0 in the base-2 representation of 6 (most significant digit first)
        self.assertEqual(get_digit(6,2,0,most_signicant_digit_first=True),1)

    def test_first_numbers_in_base_basic(self):
        # Binary numbers (least significant digit first, default)
        self.assertEqual(list(first_numbers_in_base(5,2)),[[0],[1],[0,1],[1,1],[0,0,1]])

        # Ternary numbers (least significant digit first, default)
        self.assertEqual(list(first_numbers_in_base(5,3)),[[0],[1],[2],[0,1],[1,1]])

    def test_first_numbers_in_base_most_significant_digit_first(self):
        # Binary numbers (most significant digit first)
        self.assertEqual(list(first_numbers_in_base(5,2,most_signicant_digit_first=True)),[[0],[1],[1,0],[1,1],[1,0,0]])

        # Ternary numbers (most significant digit first)
        self.assertEqual(list(first_numbers_in_base(5,3,most_signicant_digit_first=True)),[[0],[1],[2],[1,0],[1,1]])

    def test_first_numbers_in_base_with_zerofill(self):
        # Binary numbers with zero-fill (least significant digit first, default)
        self.assertEqual(list(first_numbers_in_base(5,2,zerofill_to_length=3)),
                         [[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1]])

        # Ternary numbers with zero-fill (most significant digit first)
        self.assertEqual(list(first_numbers_in_base(5,3,zerofill_to_length=3,most_signicant_digit_first=True)),[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1]])

    def test_first_numbers_in_base_large(self):
        # Binary numbers with large n (least significant digit first)
        self.assertEqual(list(first_numbers_in_base(3,2)),[[0],[1],[0,1]])

    def test_first_numbers_in_base_edge_cases(self):
        # Base case: No numbers
        self.assertEqual(list(first_numbers_in_base(0,2)),[])

        # Base case: Base = 1 (only 0s)
        #self.assertEqual(list(first_numbers_in_base(5,1)),[[0],[0],[0],[0],[0]])

    # --- Tests for number_to_list_of_digits ---

    def test_number_to_list_of_digits_basic(self):
        # Convert 6 to base 2
        self.assertEqual(number_to_list_of_digits(6,2),[0,1,1])

        # Convert 6 to base 2, most significant digit first
        self.assertEqual(number_to_list_of_digits(6,2,most_signicant_digit_first=True),[1,1,0])

    def test_number_to_list_of_digits_with_zerofill(self):
        # Convert 6 to base 2 with zero-fill to length 5 (least significant digit first)
        self.assertEqual(number_to_list_of_digits(6,2,zerofill_to_length=5),[0,0,0,1,1])

        # Convert 6 to base 2 with zero-fill to length 5 (most significant digit first)
        self.assertEqual(number_to_list_of_digits(6,2,zerofill_to_length=5,most_signicant_digit_first=True),[0,0,1,1,0])

    def test_number_to_list_of_digits_edge_cases(self):
        # Edge case: Converting 0 in any base should return [0]
        self.assertEqual(number_to_list_of_digits(0,10),[0])
        self.assertEqual(number_to_list_of_digits(0,2),[0])

        # Edge case: Converting negative numbers (raises error)
        with self.assertRaises(ValueError):
            number_to_list_of_digits(-5,10)

    # --- Tests for list_of_digits_to_number ---

    def test_list_of_digits_to_number_basic(self):
        # Convert list of digits [0, 1, 1] in base 2 back to number (least significant digit first)
        self.assertEqual(list_of_digits_to_number([0,1,1],2),6)

        # Convert list of digits [1, 1, 0] in base 2 back to number (most significant digit first)
        self.assertEqual(list_of_digits_to_number([1,1,0],2,most_signicant_digit_first=True),6)

    def test_list_of_digits_to_number_with_large_numbers(self):
        # Test with a large number
        digits=[1,0,1,0,1,1]
        base=2
        self.assertEqual(list_of_digits_to_number(digits,base),45)  # 101011 in base 2 is 45 in decimal

    def test_list_of_digits_to_number_edge_cases(self):
        # Edge case: Convert empty list of digits
        self.assertEqual(list_of_digits_to_number([],10),0)

        # Edge case: Convert list of zeros
        self.assertEqual(list_of_digits_to_number([0,0,0],10),0)

    # --- Tests for get_digit ---

    def test_get_digit_basic(self):
        # Get the digit at position 2 in the base-2 representation of 6 (least significant digit first)
        self.assertEqual(get_digit(6,2,2),1)  # 110 (binary)

        # Get the digit at position 0 in the base-2 representation of 6 (most significant digit first)
        self.assertEqual(get_digit(6,2,0,most_signicant_digit_first=True),1)

    def test_get_digit_edge_cases(self):
        # Edge case: Asking for a digit position greater than the length of the number (should return 0)
        self.assertEqual(get_digit(6,2,10),0)  # In binary, 6 is "110", so position 10 is 0

        # Edge case: Asking for digit in base 1
        self.assertEqual(get_digit(5,1,0),0)  # Base 1 only has "0" digits.

    def test_get_digit_negative_position(self):
        # Test with negative positions
        self.assertEqual(get_digit(6,2,-1),0)
        self.assertEqual(get_digit(6,2,-2),1)


if __name__=='__main__':
    unittest.main()
