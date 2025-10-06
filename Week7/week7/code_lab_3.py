# Constructor
class Student:

    first_name = ""
    last_name = ""
    is_graduated = False

    # Constructor
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def say_hi(self):
        print("Hello " + self.first_name, self.last_name)

    def format_name(self):
        return self.first_name + " " + self.last_name

student_a = Student("Sunil", "Tiwari")
student_a.say_hi()
print(student_a.format_name())
