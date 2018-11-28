from person import Person


class Teacher(Person):
    """Simple teacher class"""

    def teaches(self, student):
        """Checks if a teacher teaches a student"""
        return len(set(self.classes) & set(student.get_classes())) > 0
