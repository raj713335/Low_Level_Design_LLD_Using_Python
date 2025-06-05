class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.professors = []

    def add_professor(self, professor):
        self.professors.append(professor)

    def show_professors(self):
        print(f"Professor at {self.university_name}:")
        for professor in self.professors:
            print(f" - {professor.name}")


if __name__ == "__main__":
    prof1 = Professor("Dr Arnab", "Computer Science")
    prof2 = Professor("Dr Jayita", "AI")

    university = University("Jadavpur University")
    university.add_professor(prof1)
    university.add_professor(prof2)

    university.show_professors()

    # Professor can exist independently

    prof1.teach()
    prof2.teach()
