
"""This program demonstrates a simple Teacher class in Python.
It stores a teacher's name and subject and displays what the
teacher is teaching using an instance method.
"""
class Teacher:
    """Represent a teacher with a name and subject."""
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def teach(self):
        """Return a message describing what the teacher is teaching."""
        return f"{self.name} is teaching {self.subject}."
t1 = Teacher("Mr. Smith", "Mathematics")
print(t1.teach())
