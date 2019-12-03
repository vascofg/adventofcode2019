from day3.solve import makeGrid, closestIntersection, leastSteps
import unittest


class TestCrossedWiresDistance(unittest.TestCase):
    def test_distance1(self):
        wire1 = ["R8", "U5", "L5", "D3"]
        wire2 = ["U7", "R6", "D4", "L4"]

        self.assertEqual(closestIntersection(
            makeGrid(wire1), makeGrid(wire2)), 6)

    def test_distance2(self):
        wire1 = ["R75", "D30", "R83", "U83",
                 "L12", "D49", "R71", "U7", "L72"]
        wire2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]

        self.assertEqual(closestIntersection(
            makeGrid(wire1), makeGrid(wire2)), 159)

    def test_distance3(self):
        wire1 = ["R98", "U47", "R26", "D63", "R33",
                 "U87", "L62", "D20", "R33", "U53", "R51"]
        wire2 = ["U98", "R91", "D20", "R16",
                 "D67", "R40", "U7", "R15", "U6", "R7"]

        self.assertEqual(closestIntersection(
            makeGrid(wire1), makeGrid(wire2)), 135)

class TestCrossedWiresSteps(unittest.TestCase):
    def test_distance1(self):
        wire1 = ["R8", "U5", "L5", "D3"]
        wire2 = ["U7", "R6", "D4", "L4"]

        self.assertEqual(leastSteps(
            makeGrid(wire1), makeGrid(wire2)), 30)

    def test_steps2(self):
        wire1 = ["R75", "D30", "R83", "U83",
                 "L12", "D49", "R71", "U7", "L72"]
        wire2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]

        self.assertEqual(leastSteps(
            makeGrid(wire1), makeGrid(wire2)), 610)

    def test_steps3(self):
        wire1 = ["R98", "U47", "R26", "D63", "R33",
                 "U87", "L62", "D20", "R33", "U53", "R51"]
        wire2 = ["U98", "R91", "D20", "R16",
                 "D67", "R40", "U7", "R15", "U6", "R7"]

        self.assertEqual(leastSteps(
            makeGrid(wire1), makeGrid(wire2)), 410)