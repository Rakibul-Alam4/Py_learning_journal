"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Rakib", 85)
print(s1)
#<__main__.Student object at 0x000001232AD26A50>
#এখানে শুধু object এর memory address দেখাচ্ছে
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(name={self.name}, marks={self.marks})"

s1 = Student("Rakib", 85)
print(s1)
