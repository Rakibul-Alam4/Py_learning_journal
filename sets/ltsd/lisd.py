# list
"""
values = [1,2,3,4,4]
print(values)
values.append(5)
print("new values:", values)
"""
# Tuples
"""
values = (1, 2, 3, 4, 4)
print(values)

# 1 এর index খুঁজে বের করা
index_of_1 = values.index(1)  
print("Index of 1:", index_of_1)

# 4 এর count খুঁজে বের করা
count_of_4 = values.count(4)
print("Count of 4:", count_of_4)
"""
# sets
"""
values = {1,2,3,4,4}
print(values)
values.add(5)
values.update([6,7,8,9])
print("new values: ", values) 
"""
# dictionary

values = {
    101 : 'a',
    102 : 'b',
    103 : 'c',
}
print(values)

values[105]= 'd'
values[102]= 'g'
print("new element: ", values) 