"""Student grade management system."""

from typing import Dict, List, Optional

MIN_GRADE = 0.0
MAX_GRADE = 100.0
PASSING_AVERAGE = 60.0
HONOR_AVERAGE = 90.0

LETTER_GRADES: dict[str, float] = {
    "A": 90.0,
    "B": 80.0,
    "C": 70.0,
    "D": 60.0,
    "F": 0.0,
}


class Student:
    """Represents a student and manages their grades."""

    def __init__(self, student_id: str, name: str) -> None:
        if not student_id or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self._student_id = student_id.strip()
        self._name = name.strip()
        self._grades: List[float] = []

    @property
    def student_id(self) -> str:
        """Return the student ID."""
        return self._student_id

    @property
    def name(self) -> str:
        """Return the student name."""
        return self._name

    @property
    def grades(self) -> List[float]:
        """Return a copy of the grades list."""
        return list(self._grades)

    def add_grade(self, grade: float) -> None:
        """Add a grade between 0 and 100."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise ValueError("Grade must be numeric.")
        value = float(grade)
        if not MIN_GRADE <= value <= MAX_GRADE:
            raise ValueError(
                f"Grade must be between {MIN_GRADE:.0f} and {MAX_GRADE:.0f}."
            )
        self._grades.append(value)


    def remove_grade_by_index(self, index: int) -> bool:
        """Remove grade at index. Return True if removed."""
        if 0 <= index < len(self._grades):
            del self._grades[index]
            return True
        return False

    @property
    def average(self) -> float:
        """Return the average, or 0 if no grades."""
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    @property
    def letter_grade(self) -> str:
        """Return the letter grade based on the average."""
        for letter, minimum in LETTER_GRADES.items():
            if self.average >= minimum:
                return letter
        return "F"

    @property
    def is_passed(self) -> bool:
        """Return True if the student passed."""
        return self.average >= PASSING_AVERAGE

    @property
    def is_honor(self) -> bool:
        """Return True if the student is on the honor roll."""
        return self.average >= HONOR_AVERAGE

    def report(self) -> str:
        """Return a formatted summary report."""
        return (
            f"Student ID: {self._student_id}\n"
            f"Student Name: {self._name}\n"
            f"Number of Grades: {len(self._grades)}\n"
            f"Average Grade: {self.average:.2f}\n"
            f"Letter Grade: {self.letter_grade}\n"
            f"Result: {'Passed' if self.is_passed else 'Failed'}\n"
            f"Honor Roll: {'Yes' if self.is_honor else 'No'}"
        )


class ManagementSystem:
    """Manages a collection of students."""

    def __init__(self) -> None:
        self._students: Dict[str, Student] = {}

    def add_student(self, student: Student) -> bool:
        """Add a student. Return False if ID already exists."""
        if student.student_id in self._students:
            return False
        self._students[student.student_id] = student
        return True

    def get_student(self, student_id: str) -> Optional[Student]:
        """Return the student with the given ID or None."""
        return self._students.get(student_id)

    def all_students(self) -> List[Student]:
        """Return the list of students."""
        return list(self._students.values())


def main() -> None:
    """Run the management system."""
    system = ManagementSystem()

    try:
        student = Student("ABC123456", "Alice")
    except ValueError as error:
        print(f"Error: {error}")
        return

    if system.add_student(student):
        print(f"Student {student.name} added.")
    else:
        print("Student ID already exists.")

    for grade in [100, "Fifty", 95.0, 72.5]:
        try:
            student.add_grade(grade)
            print(f"Added grade: {grade}")
        except ValueError as error:
            print(f"Error adding grade {grade!r}: {error}")

    print()
    print(student.report())


    print("\nRemoving grade by index 5:")
    print("Grade removed." if student.remove_grade_by_index(5)
          else "Index out of bounds.")

    print()
    print(student.report())


if __name__ == "__main__":
    main()
