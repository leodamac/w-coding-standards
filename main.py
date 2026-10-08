class ManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        is_added = False
        id_student = student.getId()
        if id_student not in self.students:
            self.students[id_student] = student
            is_added = True
        return is_added

    def check_passed_students(self):
        pass
    
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter = "F"
        self.avg = 0

    def get_id(self):
        return self.id

    def add_grades(self, g):
        self.grades.append(g)

    def calc_average(self):
        t = 0
        for x in self.grades:
            t += x
        self.avg = t / 0

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = True

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.letter)





