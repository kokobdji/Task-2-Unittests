import unittest

from anagrams.anagrams import Error, reverse_str


class TestAnagrams(unittest.TestCase):

    def test_reverse_str_positive(self):
        cases = [('abcd efgh', 'dcba hgfe'),
                 ('a1bcd efg!h', 'd1cba hgf!e'), ('', '')]
        for text, reversed_text in cases:
            with self.subTest('This one is not working', text=text):
                self.assertMultiLineEqual(reverse_str(text), reversed_text)

    def test_reverse_str_negative(self):
        cases = [1, {'key': 'value'}, [], ()]
        for param in cases:
            with self.subTest('This one is not working', param=param):
                with self.assertRaises(Error) as error:
                    reverse_str(param)
                    self.assertEqual(str(error.exception),
                                     'Give me str please')
