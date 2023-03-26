from datetime import datetime
import pytest
from students import Student, get_topper


@pytest.fixture
def dummy_student():
    return Student("mubeen", datetime(1989, 5, 7), "mech", 150)


def test_student(dummy_student):
    assert dummy_student.name == "mubeen"
    assert dummy_student.branch == "mech"

def test_student_add_credit(dummy_student):
    dummy_student.add_credits(50)
    assert dummy_student.credits == 200

def test_get_credit(dummy_student):
    assert dummy_student.get_credits() == 150

def test_student_age(dummy_student):
    age = (datetime.now() - dummy_student.dob).days//365
    assert dummy_student.get_age() == age


# Here we can create multiple objects of a Student class
# this process of creating multiple objects is called factory
@pytest.fixture
def dummy_student_factory():
    def student_factory(name, credit):
        return Student(name, datetime(1989, 5, 7), "mech", credit)
    return student_factory

def test_topper(dummy_student_factory):
    students = [
        dummy_student_factory("mub1", 10),
        dummy_student_factory("mub2", 20),
        dummy_student_factory("mub3", 30),
        dummy_student_factory("mub4", 40),
    ]
    topper = get_topper(students)
    print(f"Topper of the batch = {str(topper.name)} ", end="")
    assert topper == students[3]

