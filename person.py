class Person:
    """Parent class for a teacher/student"""

    def __init__(self):
        self.classes = []
        self.quizzes = {}

    def add_class(self, class_name):
        """Adds a single class to the person"""
        # Only one class with a name permited
        if not self.has_class(class_name):
            self.classes.append(class_name)

    def has_class(self, class_name):
        """Checks if a person has a class"""
        return class_name in self.classes

    def get_classes(self):
        """Returns the classes for a person"""
        return self.classes

    def get_quizzes(self):
        """Returns the quizzes for a person"""
        return self.quizzes.values()