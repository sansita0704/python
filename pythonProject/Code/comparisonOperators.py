# Comparison Operators used to compare values.

x = 3 > 2
# Here, '3 > 2' is called a boolean expression because it produces a boolean value.

print(x)
print(3 >= 2)
print(3 <= 2)
print(3 == 2)
# '==' is called equality operator.
# We use it to compare two values for equality.
# It is different from assignment operator.

print(3 != 2)
# '!=' is called not equality operator.

# Logical Operators are used to build complex rule and conditions.

price = 25
print(price > 10 and price < 30)
# If both the boolean expressions returns true then the result of the entire expression will be true.

price = 5
print(price > 10 or price < 30)
# If one of the boolean expression  returns true then the result of the entire expression will be true.
# How python will execute the above code?
# It will first check if price > 10. No, it is not > 10.
# So, it will move to second condition i.e. price < 30.
# Yes, it is < 30 so it will return boolean true.

print(not price > 10)
# 'not' operator reverses the answer of any boolean expression.