from person import Person


class Student(Person):
    """Simple student class"""

    def add_quiz(self, quiz):
        """Adds a quiz"""
        if quiz['class_name'] in self.classes:
            self.quizzes["%s_%s" % (quiz['class_name'], quiz['quiz_name'])] = quiz
            return True
        return False

    def submit_answer(self, class_name, quiz_name, question, answer):
        if class_name in self.classes:
            quiz = self.quizzes["%s_%s" % (class_name, quiz_name)]
            if quiz:
                if not 'response' in quiz:
                    quiz['response'] = {}
                quiz['response'][question] = answer
                return True
        return False
