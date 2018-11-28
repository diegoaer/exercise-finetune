class Person:
    """Parent class for a teacher/student"""

    def __init__(self):
        self.classes = []

    def add_class(self, class_name):
        """Adds a single class to the person"""
        # Only one class with a name permited
        if not self.has_class(class_name):
            self.classes.append(class_name)

    def has_class(self, class_name):
        """Checks if a person has a class"""
        return class_name in self.classes