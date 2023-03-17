# ----------------------------------------------------------------------
# Name:      homework6
# Purpose:   implement two functions given by the instructions
# Author(s): Jessie Lyu, An Tran
# Date: 03/17/2023
# ----------------------------------------------------------------------
"""
Implementation of final_grade and most_words functions

This program consists of final_grade and most_words functions.
The final_grade function takes a dict representing student grades and
extra credit points as parameters, and returns a new dictionary that
contains the names of the students and their updated grades.
The most_words function takes an arbitrary number of strings and
returns the string with the most number of words.
"""


def final_grade(student_grade, extra_points=1):
    """
    Return a new dictionary that contains the names
    of the students and their updated grade after
    the extra credit points have been added.
    :param student_grade: (dict) dictionary of arbitrary size
    representing student grades.
    :param extra_points: (int) extra points to be added.
    :return: (dict) a new dictionary containing the updated grades
    for each student.
    """

    return {name: grade + extra_points
            for name, grade in student_grade.items()}


def most_words(*args):
    """
    Return the string with the most number of words.
    :param args: an arbitrary number of strings.
    :return: (string) the string with the most number of words.
    """

    return max(args, key=lambda word: len(word.split())) if args else None
