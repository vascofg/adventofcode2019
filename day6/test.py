from day6.solve import ocb, orbitalTransfers
import unittest


class TestOCB(unittest.TestCase):
    def test_ocb(self):
        orbits = [
            ("COM", "B"),
            ("B", "C"),
            ("C", "D"),
            ("D", "E"),
            ("E", "F"),
            ("B", "G"),
            ("G", "H"),
            ("D", "I"),
            ("E", "J"),
            ("J", "K"),
            ("K", "L")
        ]
        self.assertEqual(ocb(orbits), 42)

