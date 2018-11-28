from person import Person


class Student(Person):
    """Simple student class"""

    def add_quiz(self, quiz):
        """Adds a quiz"""
        if quiz['class_name'] in self.classes:
            self.quizzes["%s_%s" % (quiz['class_name'], quiz['quiz_name'])] = quiz
            return True
        return False
