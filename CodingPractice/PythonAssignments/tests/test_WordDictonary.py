import unittest
from CodingPractice.PythonAssignments.excercises.WordDictionary import *


def get_file_path(fn):
    import os
    return os.path.join(os.path.dirname(__file__), fn)


def get_file_contents(fn):
    f = get_file_path(fn)
    with open(f,'r') as fh:
        return fh.read()


class TestLocalDictionary(unittest.TestCase):

    def test_01_get_file_path(self):
        a = LocalDictionary.get_file_path('LocalDictionary.csv')

        self.assertEqual('/Users/hannah/Documents/Dev/source/PracticePython'
                         '/CodingPractice/PythonAssignments/excercises'
                         '/LocalDictionary.csv', a)

    def test_02_make_list_of_word_definitions(self):
        a = LocalDictionary.make_list_of_word_definitions('LocalDictionary.csv')

        self.assertEqual([['doe', 'A deer a female deer'],
                            ['ray', 'A drop of golden sun'],
                            ['me', 'A name I call myself'],
                            ['fa', 'A long long way to run'],
                            ['sew', ' A needle pulling thread'],
                            ['la', 'A word to follow sew'],
                            ['tee', 'A drink with jam and bread']],
                         a)

    def test_03_get_definition_known_word(self):
        a = LocalDictionary('LocalDictionary.csv')

        self.assertEqual(['A deer a female deer'], a.look_up('doe'))

    def test_04_get_definition_fail(self):
        a = LocalDictionary('LocalDictionary.csv')

        self.assertEqual(['Hello not found in LocalDictionary'], a.look_up('Hello'))

    def test_05_get_json(self):

        data = get_file_contents('AceExample.json')

        a = OxfordDictionary.get_definitions(data)

        self.assertEqual(["playing card with single spot on it, ranked as highest card in its suit in most card games",
                          "person who excels at particular sport or other activity",
                          "(in tennis and similar games) service that opponent is unable to return and thus wins point",
                          "asexual person",
                          "very good",
                          "asexual",
                          "(in tennis and similar games) serve ace against",
                          "achieve high marks in"],
                         a)

    @unittest.skip("Hits the internet.")
    def test_06_Oxford_lookup(self):

        a = OxfordDictionary()

        self.assertEqual(["playing card with single spot on it, ranked as highest card in its suit in most card games",
                          "person who excels at particular sport or other activity",
                          "(in tennis and similar games) service that opponent is unable to return and thus wins point",
                          "asexual person",
                          "very good",
                          "asexual",
                          "(in tennis and similar games) serve ace against",
                          "achieve high marks in"],
                         a.look_up('ace'))


if __name__ == '__main__':
    unittest.main()
