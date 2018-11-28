import pytest

from student import Student


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
