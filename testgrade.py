# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement a fictional online store
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------

import unittest
import grade


class TestFinalGrade(unittest.TestCase):
    """
    Test case for the normal execution of final_grade method
    """
    def setUp(self):
        """Create dictionaries for testing"""
        self.default_dict = {'Lisa': 85, 'Tom': 90, 'Alex': 70}
        self.empty_dict = {}
        self.non_empty_dict = {15: 'Adam', (1, 2): 124, 'Will': 'Charlie'}

    def test_final_grade_default(self):
        new_grades = grade.final_grade(self.default_dict)
        self.assertEqual(new_grades, {'Lisa':
                         86, 'Tom': 91, 'Alex': 71})
        self.assertNotEqual(self.default_dict, new_grades)

    def test_final_grade_empty(self):
        self.assertEqual(grade.final_grade(self.empty_dict, 3), {})
        self.assertEqual(self.empty_dict, {})

    def test_final_grade_non_empty(self):
        new_grades = grade.final_grade(self.default_dict, 5)
        self.assertEqual(new_grades, {'Lisa': 90, 'Tom': 95, 'Alex': 75})
        self.assertNotEqual(self.default_dict, new_grades)


class TestMostWords(unittest.TestCase):
    """
    Test case for the nomral execution of most_words method
    """
    def setUp(self):
        """Create strings for testing"""
        self.str1 = 'hello'
        self.str2 = 'i like ice cream'
        self.str3 = "where's my super suit"
        self.str4 = 'this is a really really really long string'
        self.str5 = 'im hungry'
        self.str6 = 'school is so fun'
        self.str7 = "it's time to go home now"
        self.str8 = 'how was your day'
        self.str9 = 'your punctuation is incorrect'

    def test_most_words_no_args(self):
        self.assertEqual(grade.most_words(), None)

    def test_most_words_one_arg(self):
        self.assertEqual(grade.most_words('hello'), 'hello')

    def test_most_words_arbitrary_args(self):
        self.assertEqual(grade.most_words(self.str1, self.str2, self.str3,
                                          self.str4, self.str5, self.str6,
                                          self.str7, self.str8, self.str9),
                         'this is a really really really long string')


if __name__ == '__main__':
    unittest.main()
