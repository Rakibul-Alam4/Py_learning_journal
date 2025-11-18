numbers = [1,2,3,4,5]

first = set(numbers)
second = {2,6}

print(first | second)
print (first & second)
print (first - second)
print(first ^ second)
if 1 in first:
    print("yes") 