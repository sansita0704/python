# Tuples are used to store a sequence of objects just like lists but tuples are immutable.
# So, they can't be changed once they are created.
# We use [] to define a list and () to define a tuple.

numbers = (1, 2, 3, 3)
# numbers[0] = 10
# If we try to re-assign 1st element of the tuple we will get an error.
# That's why, we do not have methods like append, remove, etc. for tuples.

print(numbers.count(3))
# count method returns the no. of occurrences of an element.

print(numbers.index(3))
# index method returns the index of first occurrence of an element.

# The other methods which start with an underscore are called magic methods.
# We use tuples if, in a program, we do not want anyone to accidentally modify the sequence of numbers.