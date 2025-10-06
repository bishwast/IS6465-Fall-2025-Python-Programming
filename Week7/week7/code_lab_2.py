# Wk 7 Code Along 2
class SimpleClass:
    pass

class YesNoBooleanValueConverter(SimpleClass):

    def convert(self, val):
        if val:
            return "Yes"
        else:
            return "No"

    def convertBack(self, val):
        val = str(val).upper()
        if val == "Y" or val == "YES":
            return True
        else:
            return False

class Student:

    first_name = ""
    last_name = ""
    is_graduated = False

# Instance of a class
student_a = Student()
student_a.first_name = "Sunil"
student_a.last_name = "Tiwari"
student_a.is_graduated = True

val_converter = YesNoBooleanValueConverter()
grad_status = val_converter.convert(student_a.is_graduated)
print(grad_status)

# Convert back
grad_status1 = val_converter.convertBack("N")
print(student_a.first_name, student_a.last_name, "Is graduated: ", val_converter.convert(grad_status1))