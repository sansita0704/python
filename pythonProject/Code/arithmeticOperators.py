# Arithmetic Operators in python are same as maths.
print(10 + 30)
print(10 - 30)
print(10 * 30)

# We have two types of division operators:

print(30 / 10)
# Returns a float value.
# If the result is an integer then also it will display as a float.

print(10 // 30)
# Returns an integer value.

print(30 % 10)
# Returns the remainder of the division.

print(10 ** 3)
# '**' is an exponent operator.
# '10 ** 3' means 10 to the power 3.

# Augmented assignment operator

x = 10
x = x + 3
x += 3
# We have an assignment operator and then we have augmented or enhanced it by adding an addition operator before it.

x -= 3
print(x)

# Operator Precedence:
# It is a concept which determines the order in which different operators are applied.
# BODMAS

a = 10 + 3 * 2
print(a) 

b = (10 + 3) * 2
# We can change the operator precedence using parenthesis.