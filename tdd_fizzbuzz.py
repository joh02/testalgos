'''
example für TDD: fizz buzz challange:
schreibe eine Funktion, die eine pos int n übernimmt und einen str returned
fizz wenn n Vielfaches von 3 ist
buzz wenn n Vielfaches von 5 ist
fizzbuzz wenn n Vielfaches von 3 und 5 ist ()
sonst ""
'''

import unittest

def fb_func(n):
    if not n%(3*5):
        return 'fizzbuzz'

    elif not n%3:
        return 'fizz'
    elif not n%5:
        return 'buzz'
    return ''

class Test_fb_func(unittest.TestCase):
    def test_retString(self):
        for n in range(17):
            self.assertEqual(type(fb_func(n)), str)
            self.assertTrue(fb_func(n) in ['fizz', 'buzz', '', 'fizzbuzz'])

    def test_3(self):
        self.assertEqual('fizz', fb_func(3))

    def test_5(self):
        self.assertEqual('buzz', fb_func(5))

    def test_15(self):
        self.assertEqual('fizzbuzz', fb_func(15))

    def test_other2(self):
        self.assertEqual('', fb_func(2))


    def test_other(self):
        for n in range(20):
            if n%3
        self.assertEqual('', fb_func(2))


if __name__ == '__main__':
    unittest.main()
