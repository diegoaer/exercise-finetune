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

    def test_teacher_create_quiz(self):
        """Tests if a teacher can create a quiz"""
        teacher = Teacher()
        teacher.add_class('math')
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
        teacher.create_quiz('math', 'quiz1', questions)
        assert len(teacher.get_quizzes()) == 1

    def test_not_teacher_create_quiz(self):
        """Tests if a teacher cant create a quiz without right answers"""
        teacher = Teacher()
        teacher.add_class('math')
        questions = {'1 + 1?': {'1': False, '2': False, '3': False}}
        assert not teacher.create_quiz('math', 'quiz1', questions)

    def test_teacher_create_quizzes(self):
        """Tests if a teacher can create multiple quizzes"""
        teacher = Teacher()
        teacher.add_class('math')
        teacher.add_class('science')
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
        teacher.create_quiz('math', 'quiz1', questions)
        questions = {'1 + 1?': {'1': False, '2': True, '3': False}}
        teacher.create_quiz('science', 'quiz1', questions)
        print(teacher.get_quizzes())
        assert len(teacher.get_quizzes()) == 2

    def test_teacher_assign_quiz(self):
        """Tests if a teacher can assign a quiz to a student"""
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
        assert teacher.assign_quiz(student, 'math', 'quiz1')

    def test_not_teacher_assign_quiz(self):
        """Tests if a teacher can't assign a uuiz to a student that is not in his class"""
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
        assert not teacher.assign_quiz(student, 'math', 'quiz1')

    def test_teacher_grade_quiz(self):
        """Tests if a teacher quiz can be graded"""
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
        student.submit_answer('math', 'quiz1', 0, 0)
        student.submit_answer('math', 'quiz1', 0, [1, 2])
        assert teacher.grade(student, student.get_quiz('math', 'quiz1'))

    def test_teacher_compute_total(self):
        """Tests if a teacher can compute the total for a student"""
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
        student = Student('Sam')
        student.add_class('math')
        teacher.assign_quiz(student, 'math', 'quiz1')
        student.submit_answer('math', 'quiz1', 0, 0)
        student.submit_answer('math', 'quiz1', 0, [1, 2])
        teacher.grade(student, student.get_quiz('math', 'quiz1'))
        assert teacher.total(student.get_name()) == 50
