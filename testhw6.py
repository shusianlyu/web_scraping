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
    def test_default_argument(self):
        """Test if the default argument is equal to 1"""
        # original grades dict
        grades = {'Jessie': 85, 'An Tran': 90}
        # new updated grades dict
        update_grades = homework6.final_grade(grades)
        # expected grades dict after calling the method
        expected_grades = {'Jessie': 86, 'An Tran': 91}
        self.assertEqual(update_grades, expected_grades)

    def test_empty_dictionary(self):
        """Test an update on empty dictionary"""
        # original grades dict
        grades = {}
        # new updated grades dict
        update_grades = homework6.final_grade(grades)
        self.assertEqual(update_grades, {})

    def test_non_empty_dictionary(self):
        """Test an update on a non-empty dictionary"""
        # original grades dict
        grades = {'Jessie': 85, 'An Tran': 90}
        # new updated grades dict
        update_grades = homework6.final_grade(grades, 2)
        # expected grades dict after calling the method
        expected_grades = {'Jessie': 87, 'An Tran': 92}
        self.assertEqual(update_grades, expected_grades)
        # check that the original dictionary has not been modified
        self.assertNotEqual(grades, update_grades)


class TestMostWords(unittest.TestCase):

    """
    Test case for the normal execution of the most_words method
    """

    def test_no_arguments(self):
        """Test on function with no arguments"""
        self.assertIsNone(homework6.most_words())

    def test_one_argument(self):
        """Test on function with one argument"""
        self.assertEqual(homework6.most_words("Test"), "Test")

    def test_many_arguments(self):
        """Test on function with many arguments"""
        self.assertEqual(homework6.most_words("Test", "Hello",
                                              "Prof. Jessie"), "Prof. Jessie")


if __name__ == '__main__':
    unittest.main()
