"""
def reverse_string(s):
    return s[::-1]  # s[start:stop:step]

print(reverse_string("jhc kh"))
"""
def reverse_string(s):
    return "".join(reversed(s))

print(reverse_string("Python"))