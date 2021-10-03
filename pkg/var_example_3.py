# ------------------------------------------------------
# Top level commentingon a file.  A short line or two of
# Description no longr than 72 characters.
#
# (C) 2021 Ruth Lennon, LYIT
# Available under GNU public license
# ------------------------------------------------------

student_name = "Iordanis Sidiropoulos"
student_name = "iordAnis Sidiropoulos"  # fixes the error

studentA_grade = 77
studentB_grade = 77
studentC_grade = [77]  # array of integers
studentD_grade = [77]
studentE_grade = studentC_grade


print(studentA_grade is studentB_grade)  # They are the same object type & value
print(studentA_grade == studentB_grade)  # They have the same value

print(studentC_grade is studentD_grade)  # note the same object => False
print(studentC_grade == studentD_grade)  # true as the value is the same
print(studentC_grade is studentE_grade)
print(studentE_grade)