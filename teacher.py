from person import Person


class Teacher(Person):
    """Simple teacher class"""

    def teaches(self, student):
        """Checks if a teacher teaches a student"""
        return len(set(self.classes) & set(student.get_classes())) > 0

    def create_quiz(self, class_name, quiz_name, questions):
        """Creates a quiz"""
        if not class_name in self.classes:
            return False
        for answers in questions.values():
            if not True in answers.values():
                return False
        self.quizzes["%s_%s" % (class_name, quiz_name)] = {
            'class_name': class_name,
            'quiz_name': quiz_name,
            'questions': questions
        }
        return True

    def assign_quiz(self, student, class_name, quiz_name):
        """Assign, previously saved, a quiz to a student"""
        quiz = self.quizzes["%s_%s" % (class_name, quiz_name)]
        if self.teaches(student) and quiz:
            return student.add_quiz(quiz)
        return False