import unittest

def decimal_to_binary(num):
    """
    Convert a decimal number to binary and return the binary representation.

    Parameters:
    num (int): The decimal number to be converted to binary.

    Returns:
    str: The binary representation of the input decimal number.
    """
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    if num == 0:
        return '0'
    binary = ''
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

class TestDecimalToBinary(unittest.TestCase):
    def test_positive_decimal(self):
        result = decimal_to_binary(10)
        print(f"Decimal 10 in binary: {result}")
        self.assertEqual(result, '1010')

    def test_zero_decimal(self):
        result = decimal_to_binary(0)
        print(f"Decimal 0 in binary: {result}")
        self.assertEqual(result, '0')

    def test_negative_decimal(self):
        with self.assertRaises(ValueError):
            print("Testing negative decimal input")
            decimal_to_binary(-5)

if __name__ == '__main__':
    unittest.main()