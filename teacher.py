from person import Person


class Teacher(Person):
    """Simple teacher class"""

    def __init__(self):
        super().__init__()
        self.grades = {}

    def teaches(self, student):
        """Checks if a teacher teaches a student"""
        return len(set(self.classes) & set(student.get_classes())) > 0

    def create_quiz(self, class_name, quiz_name, questions):
        """Creates a quiz"""
        if not class_name in self.classes:
            return False
        for question in questions.values():
            if not True in question.values():
                return False
        self.quizzes["%s_%s" % (class_name, quiz_name)] = {
            'class_name': class_name,
            'quiz_name': quiz_name,
            'questions': questions
        }
        return True

    def assign_quiz(self, student, class_name, quiz_name):
        """Assign, previously saved, a quiz to a student"""
        quiz = self.quizzes["%s_%s" % (class_name, quiz_name)].copy()
        if self.teaches(student) and quiz:
            return student.add_quiz(quiz)
        return False

    def grade(self, student, quiz):
        """Grade a test and save the result"""
        if self.teaches(
                student) and 'response' in quiz and quiz['class_name'] in student.get_classes():
            # For simplicity every question has the same value in points, and every quiz is valued
            # @ 100 points
            points_per_question = 100.0 / len(quiz['questions'])
            total = 0
            for question in quiz['questions'].keys():
                response = quiz['response'][question]
                if type(response) == int:
                    response = [response]
                correct = True
                for answer in response:
                    correct &= quiz['questions'][question][answer]
                if correct:
                    total += points_per_question
            quiz['total'] = total
            if not student.get_name() in self.grades:
                self.grades[student.get_name()] = {'quizzes': {}}
            quiz_key = "%s_%s" % (quiz['class_name'], quiz['quiz_name'])
            self.grades[student.get_name()]['quizzes'][quiz_key] = quiz
            return total
        return False

    def total(self, student_name, class_name):
        """Gets the total for a student in a class"""
        if student_name in self.grades and 'quizzes' in self.grades[student_name]:
            total = 0
            for quiz in self.grades[student_name]['quizzes'].values():
                total += quiz['total']
            return total
        return False
