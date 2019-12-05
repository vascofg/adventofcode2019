from day4.solve import isValidPassword, isValidPassword2
import unittest


class TestPasswords(unittest.TestCase):
    def test_password1(self):
        self.assertTrue(isValidPassword("111111"))

    def test_password2(self):
        self.assertFalse(isValidPassword("223450"))

    def test_password3(self):
        self.assertFalse(isValidPassword("123789"))

class TestPasswords2(unittest.TestCase):
    def test_password1(self):
        self.assertTrue(isValidPassword2("112233"))

    def test_password2(self):
        self.assertFalse(isValidPassword2("123444"))

    def test_password3(self):
        self.assertTrue(isValidPassword2("111122"))

    def test_password4(self):
        self.assertFalse(isValidPassword2("111123"))