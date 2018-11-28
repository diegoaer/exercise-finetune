import pytest

from teacher import Teacher
from student import Student


class TestTeacher:
    """Class that contains teacher tests"""

    def test_teacher_teach_class(self):
        """Test that a teacher can teach a class"""
        teacher = Teacher()
        teacher.add_class('math')
        assert teacher.has_class('math')

    def test_teacher_teach_classes(self):
        """Test that a teacher can teach multiple classes"""
        teacher = Teacher()
        teacher.add_class('math')
        teacher.add_class('science')
        assert teacher.has_class('math') and teacher.has_class('science')

    def test_student_in_teacher_class(self):
        """Test if a student is part of a teacher's class"""
        teacher = Teacher()
        teacher.add_class('math')
        student = Student()
        student.add_class('math')
        assert teacher.teaches(student)

    def test_student_not_in_teacher_class(self):
        """Test if a student is not part of a teacher's class"""
        teacher = Teacher()
        teacher.add_class('math')
        student = Student()
        student.add_class('science')
        assert not teacher.teaches(student)
