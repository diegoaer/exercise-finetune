import pytest

from student import Student
from teacher import Teacher


class TestStudent:
    """Class that contains student tests"""

    def test_student_in_class(self):
        """Test that a student can exists in a class"""
        student = Student()
        student.add_class('math')
        assert student.has_class('math')

    def test_student_in_classes(self):
        """Test that a student can have multiple classes"""
        student = Student()
        student.add_class('math')
        student.add_class('science')
        assert student.has_class('math') and student.has_class('science')

    def test_student_answer_quiz(self):
        """Test that a student can answer a quiz"""
        teacher = Teacher()
        questions = {
            '1 + 1?': {
                '1': False,
                '2': True,
                '3': False
            },
            'name?': {
                'my name': True,
                'your name': True,
                'no name': False
            }
        }
        teacher.add_class('math')
        teacher.create_quiz('math', 'quiz1', questions)
        student = Student()
        student.add_class('math')
        teacher.assign_quiz(student, 'math', 'quiz1')
        assert student.submit_answer('math', 'quiz1', 0, 0) and student.submit_answer(
            'math', 'quiz1', 0, [1, 2])
