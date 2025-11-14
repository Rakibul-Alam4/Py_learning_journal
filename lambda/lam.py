"""
numbers = [44, 23, 2, 3, 7, 4]
# numbers.sort(reverse=True)
print(sorted(numbers)) # reverse=True
print(numbers)
"""

items = [
    ("product 25"),
    ("product 2"),
    ("product 12"),
]

# def sort_items(items):
#     return [1]
# items.sort(key=sort_items)

items.sort(key= lambda items: items [1])

print(items)

