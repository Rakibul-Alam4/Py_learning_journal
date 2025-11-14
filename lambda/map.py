items = [
    ("product", 10),
    ("product", 20),
    ("product", 30),

]
# prize = []

# for items in items:
#     prize.append(items [1])

prize = list(map(lambda items: items[1], items))
print(prize)
