from day1.solve import fuel, realfuel
import unittest

class TestFuelCalculationMethods(unittest.TestCase):
    def test_fuel1(self):
        self.assertEqual(fuel(12), 2)
    def test_fuel2(self):
        self.assertEqual(fuel(14), 2)
    def test_fuel3(self):
        self.assertEqual(fuel(1969), 654)
    def test_fuel4(self):
        self.assertEqual(fuel(100756), 33583)

class TestRealFuelCalculationMethods(unittest.TestCase):
    def test_realfuel1(self):
        self.assertEqual(realfuel(14), 2)
    def test_realfuel2(self):
        self.assertEqual(realfuel(1969), 966)
    def test_realfuel3(self):
        self.assertEqual(realfuel(100756), 50346)