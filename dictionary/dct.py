# Dictionary তৈরি
student = {
    "name": "Rakib",
    "age": 23,
    "dept": "CSE"
}

# Value access করা
print(student["name"])   # Output: Rakib
print(student["age"])    # Output: 23

# নতুন key-value যোগ করা
student["id"] = 101

# Value পরিবর্তন করা
student["age"] = 24

# Dictionary এর সব key
print(student.keys())  

# Dictionary এর সব value
print(student.values())  

# Key-Value pair
print(student.items())
