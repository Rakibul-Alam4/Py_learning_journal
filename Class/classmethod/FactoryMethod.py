class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, string_data):
        name, marks = string_data.split("-")
        return cls(name, int(marks))  # নতুন object তৈরি করবে

# Object বানানো normal way
s1 = Student("Rakib", 85)

# Object বানানো classmethod দিয়ে
s2 = Student.from_string("Hasan-90")

print(s1.name, s1.marks)  # Rakib 85
print(s2.name, s2.marks)  # Hasan 90
