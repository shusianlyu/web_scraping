# ----------------------------------------------------------------------
# Name:      testhw6
# Purpose:   implement unit test for two functions in an unittest module
# Author(s): Jessie Lyu, An Tran
# Date: 03/17/2023
# ----------------------------------------------------------------------
"""
Implementation of a unit test for two functions in an unittest module

This program consists of two test cases, one for final_grade, the
other one for most_words method.
Each test case includes 3 test methods given by the instruction.
"""

import unittest
import homework6


class TestFinalGrade(unittest.TestCase):

    """
    Test case for the normal execution of the final_grade method
    """

    def setUp(self):
        """Create dictionaries for testing"""
        # original grades dict
        self.default_dic = {'Lisa': 85, 'Tom': 90, 'Alex': 70}
        # empty dictionary
        self.empty_dic = {}
        # non empty dict
        self.non_empty_dict = {'Lisa': 85, 'Tom': 90, 'Alex': 70, 'Rose': 30}

    def test_default_argument(self):
        """Test if the default argument is equal to 1"""
        # new updated grades dict
        update_grades = homework6.final_grade(self.default_dic)
        # expected grades dict after calling the method
        expected_grades = {'Lisa': 86, 'Tom': 91, 'Alex': 71}
        self.assertEqual(update_grades, expected_grades)
        # test on undesired effect
        self.assertNotEqualEqual(update_grades, self.default_dic)

    def test_empty_dictionary(self):
        """Test an update on empty dictionary"""
        # new updated grades dict
        update_grades = homework6.final_grade(self.empty_dic, 3)
        self.assertEqual(update_grades, {})
        # test on undesired effect
        self.assertEqual(self.empty_dic, {})

    def test_non_empty_dictionary(self):
        """Test an update on a non-empty dictionary"""
        # new updated grades dict
        update_grades = homework6.final_grade(self.default_dic, 2)
        # expected grades dict after calling the method
        expected_grades = {'Lisa': 87, 'Tom': 92, 'Alex': 72}
        self.assertEqual(update_grades, expected_grades)
        # check that the original dictionary has not been modified
        self.assertNotEqual(self.default_dic, update_grades)


class TestMostWords(unittest.TestCase):

    """
    Test case for the normal execution of the most_words method
    """

    def setUp(self):
        """Create strings for testing"""
        self.str1 = "Test"
        self.str2 = "Hello"
        self.str3 = "trying my best"
        self.str4 = "is there anything i can improve on?"

    def test_no_arguments(self):
        """Test on function with no arguments"""
        self.assertIsNone(homework6.most_words())

    def test_one_argument(self):
        """Test on function with one argument"""
        self.assertEqual(homework6.most_words(self.str1), self.str1)

    def test_many_arguments(self):
        """Test on function with many arguments"""
        self.assertEqual(homework6.most_words(self.str1, self.str2,
                                              self.str3, self.str4), self.str4)


if __name__ == '__main__':
    unittest.main()
