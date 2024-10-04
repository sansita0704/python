course = "Python for Beginners"
# The string in python are technically objects.
# Objects in python are like real-world objects.
# We can think of it as a remote which has some functionalities like on and off the TV, changing the volume of the remote,etc.
# Here, this course variable is storing a string object.
# Similar to a remote, it also has some capabilities.
# These capabilities are basically functions just like input() and print().
# The difference is that input() and print() are general purpose functions i.e. they are not specific for any type of objects.
# But upper(), capitalize(), etc are specific to string objects.
# When the functions are associated to objects then they are called methods.

# 'course.upper()' - This returns the string with all of its characters in upper case

print(course.upper())
# This upper method does not change our original string, it returns a new string.

print(course)
print(course.lower())
print(course.find('a'))
# returns -1 i.e. course does not have a letter 'a'.

print(course.find(' '))
print(course.find('for'))
print(course.find('y'))
# returns first occurrence of the letter y in the string course.

# Python is case-sensitive so if we pass 'Y' in find() then it will return -1.
print(course.find('Y'))

print(course.replace('for', '4'))
# Replaces the string 'for' with a string '4'.
# Just like the upper method, the replace method does not modify the original string.

print(course.replace('Y', 'y'))
# Since, we do not have Y in the string so nothing will happen.

# Strings in python and many other programming languages are immutable, i.e. once a string is created, it cannot be modified.
# Any operation that modifies it, actually creates a new string.

# One way to find a sequence of character in a string is by using the find method.
# Another way is to use 'in' operator.

print('Python' in course)
# This return a boolean value which is desired in most of the cases.