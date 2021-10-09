from tempt import Temperature
import unittest

class kelvin_test(unittest.TestCase):
    def test_celsius(self):
        self.assertEqual(Temperature(celsius=3).kelvin,276.15)
    def test_fahrenheit(self):
        self.assertEqual(Temperature(fahrenheit=2).kelvin,256.4833)
    def test_kelvin(self):
        self.assertEqual(Temperature(kelvin=-1).kelvin,0)
    def same_kelvin(self):
        self.assertEqual(Temperature(kelvin=1).kelvin,1)

if __name__ == '__main__':
    unittest.main()