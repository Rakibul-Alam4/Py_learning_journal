from pprint import pprint

sentence = "This is a common interview question"

char_frequency = {}

for char in sentence:
    if char == " ":   #  space হলে skip করব
        continue

    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# frequency অনুযায়ী sort করা
char_frequency_sorted = sorted(char_frequency.items(),
                               key=lambda kv: kv[1],
                               reverse=True)

# সবচেয়ে বেশি আসা letter
print("Most frequent character:", char_frequency_sorted[0])

# পুরো frequency সুন্দরভাবে দেখা
pprint(char_frequency_sorted)
