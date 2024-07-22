import unittest
from marlonpy.marlonpy.Conversions.ConversionIeee import ieee754
from marlonpy.marlonpy.Conversions.ConversionBinary import binary_to_decimal

class TestConversions(unittest.TestCase):
    def test_ieee754(self):
        num = '01000010101010100100000000000000'
        result = ieee754(num)
        self.assertAlmostEqual(result, 85.125, places=3)

    def test_binary_to_decimal(self):
        binary = '101'
        result = binary_to_decimal(binary)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
