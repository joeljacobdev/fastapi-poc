
class College:
    name = None

class DepartmentBatch:
    college = None
    batch: int

# thru
class Course:
    department_batch = None
    student = None

class Student:
    name = None
