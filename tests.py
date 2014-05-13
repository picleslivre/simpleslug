# coding: utf-8
import unittest

from simpleslug import slugfy


class simpleslugTests(unittest.TestCase):

    def test_slugfy(self):
        result = slugfy('São Paulo Futebol Clube')

        self.assertEqual('sao-paulo-futebol-clube', result)

    def test_slugfy_multiple_white_spaces(self):
        result = slugfy('São  Paulo    Futebol Clube')

        self.assertEqual('sao-paulo-futebol-clube', result)

    def test_slugfy_differente_separator(self):
        result = slugfy('São Paulo Futebol Clube', separator='#')

        self.assertEqual('sao#paulo#futebol#clube', result)

    def test_slugfy_realy_crazy_chars(self):
        result = slugfy('must be empty of crazy chars @çÇ&$%^&*()-_+=¡£¢§¶•–‘“÷≥≤')

        self.assertEqual('must-be-empty-of-crazy-chars-cc', result)

    def test_slugfy_realy_crazy_chars(self):
        result = slugfy('   without separators in the begining and end of a string   ')

        self.assertEqual('without-separators-in-the-begining-and-end-of-a-string', result)