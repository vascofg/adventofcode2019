from day2.solve import compute
import unittest


class TestIntcodeComputationMethods(unittest.TestCase):
    def test_compute(self):
        codes = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expectedOutput = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(compute(codes), expectedOutput)

    def test_compute2(self):
        codes = [1, 0, 0, 0, 99]
        expectedOutput = [2, 0, 0, 0, 99]
        self.assertEqual(compute(codes), expectedOutput)

    def test_compute3(self):
        codes = [2, 3, 0, 3, 99]
        expectedOutput = [2, 3, 0, 6, 99]
        self.assertEqual(compute(codes), expectedOutput)

    def test_compute4(self):
        codes = [2, 4, 4, 5, 99, 0]
        expectedOutput = [2, 4, 4, 5, 99, 9801]
        self.assertEqual(compute(codes), expectedOutput)

    def test_compute5(self):
        codes = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        expectedOutput = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(compute(codes), expectedOutput)