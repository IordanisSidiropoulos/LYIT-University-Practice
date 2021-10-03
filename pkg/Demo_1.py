# --------------------------------------------
#
#
# (C) 2021 Ruth Lennon, LYIT
# Available under the GNU public license (GPL
# -------------------------------------------

# my_var = 10
# my_var2 = 'A'
# my_var3 = "This string is too long to really consider"

students_age = 21
students_middle_initial = 'Α'
transcript_statement = "This string is too long to really consider"
transcript_statement2 = '''This string is too long to really consider This string is too long to really consider
                       This string is too long to really considerThis string is too long to really consider  
                       This string is too long to "really considerThis string" is too long to really consider'''

print(students_age + 10)
print(students_middle_initial)
# ERROR EXAMPLE: print(students_middle_initial+10)

print(students_middle_initial + "10")
print(transcript_statement2)

print(students_middle_initial + " BC")

print()
print("{0}".format(12345678))
print("{0:10d}".format(12345678))
print("Nice {0:<15d} line of left aligned numbers".format(12345678))
print("Nice {0:>20d} line or right aligned numbers".format(12345678))
print("Nice {0:^20d} line of centered aligned numbers".format(12345678))
print("Nice {0:^20.2f} line of centered aligned numbers".format(12345678.987654))
print("{0}, {1}".format(123, 456))
print("{1}, {0}".format(123, 456))

print()

val_1 = "Iron"
val_2 = "Maiden"
print("{0}, {1}".format(val_1, val_2))
