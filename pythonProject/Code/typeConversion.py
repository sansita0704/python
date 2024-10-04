# We have learnt three types of data in python
# 1. Numbers: 10, 30.8
# 2. String: "Hello World"
# 3. Boolean: True or False

birth_year = input("Enter your birth year: ")

# To calculate the age of the user
# age = 2024 - birth_year

# The expression '2024 - birth_year' returns a value which we are storing in age variable.
# There is an error here because input function by-default returns any value as a string even if enter a number.
# "2006" and 2006 are completely different data types and python doesn't know how to subtract two different data types so we cannot subtract them.
# We need to convert the string in an integer.
# We can do it using int function which converts the data type passed in it to an integer.

age = 2024 - int(birth_year)
# Here, we are passing birth_year in int function.
# Then, subtracting the returned value from 2024.
# Then, storing the final answer in age variable.

print(age)

# Numbers having a decimal point are called float numbers in programming.
# e.g. - 10 is an integer and 10.1 is a float.
# We have float() to convert a given data type to float data type.
# Similarly, we have bool() and str() for converting a given to value to boolean and string respectively.

# Exercise

first = input("First: ")
# This line is equivalent to: first = "10"

second =  input("Second: ")
# second = "20"

# sum = first + second
# Here, if we enter 10 as first and 20 as second then instead of getting 30, we get 1020
# This happens because input() returns a string i.e. "10" and "20"
# So, here instead of adding 10 and 20, there is concatenation of strings "10" and "20"
# That's why the sum = "1020"

sum = float(first) + float(second)
# If we use int() and then enter a float value then we will get an error.
# So, we are using float(). So, if we enter int value then also it will be converted to float.
# Then it will be stored in the respective variable.
# e.g. - a = float("3") then a = 3.0

print("Sum: " + str(sum))
# Here, we use str() because sum is a float no. and we cannot add float to a string.
# So, we first convert float to string then concatenate those two strings.

# We can also write above code as:

first = float(input("First:" ))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))