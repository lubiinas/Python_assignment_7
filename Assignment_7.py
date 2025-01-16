#QUESTION 1:
# Base class
# class Course:
#     def __init__(self, course_code, course_name, credit_hours):
#         self.course_code = course_code
#         self.course_name = course_name
#         self.credit_hours = credit_hours
#
#     def display_course_info(self):
#         return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"
#
#
# # Subclass for core courses
# class CoreCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, required_for_major):
#         super().__init__(course_code, course_name, credit_hours)
#         self.required_for_major = required_for_major
#
#     def display_course_info(self):
#         status = "Required for Major" if self.required_for_major else "Not Required for Major"
#         return super().display_course_info() + f", {status}"
#
#
# # Subclass for elective courses
# class ElectiveCourse(Course):
#     def __init__(self, course_code, course_name, credit_hours, elective_type):
#         super().__init__(course_code, course_name, credit_hours)
#         self.elective_type = elective_type
#
#     def display_course_info(self):
#         return super().display_course_info() + f", Elective Type: {self.elective_type}"
#
#
# # Example usage
# if __name__ == "__main__":
#     # Creating a core course
#     core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
#     print(core_course.display_course_info())
#
#     # Creating an elective course
#     elective_course = ElectiveCourse("ENG201", "Creative Writing", 2, "liberal arts")
#     print(elective_course.display_course_info())

#QUESTION2:
from employee import Employee

# Create an object of the Employee class
employee = Employee("John Doe", 50000)

# Display the employee's name and salary
print(f"Employee Name: {employee.get_name()}")
print(f"Employee Salary: {employee.get_salary()}")

