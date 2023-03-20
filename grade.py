# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement a fictional online store
# Author(s): Jessie Lyu, An Tran
# ----------------------------------------------------------------------

def final_grade(student_grades, extra_credit=1):
    """
    calculate new grades for students after adding extra credit
    :param student_grades: (dict) where keys are students and values are
    current grades
    :param extra_credit: (int) amount of extra credit to add
    :return: (dict) where keys are students and values are updated grades
    """
    return {student: grade for student, grade in student_grades}


def most_words(*args):
    """
    out of an arbitrary amount of strings, calculate one with the highest
    number
    of words
    :param args: arbitrary amount of strings
    :return: (string) string with highest number of words
    """
    if args:
        return max(args, key=lambda x: len(x.split()))

