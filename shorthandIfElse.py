a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# result = value_if_true if condition else value_if_false

# This syntax is equivalent to the following if-else statement:

# if condition:
#     result = value_if_true
# else:
#     result = value_if_false