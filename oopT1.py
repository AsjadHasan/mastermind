class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}."

t1 = Teacher("Mr. Smith", "Mathematics")
print(t1.teach())