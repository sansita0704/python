# int, float, boolean and string are called primitive or basic data types in python.
# We also have some complex data types in python.
# We use lists to represent lists of objects.

names = ["John", "Sam", "Sansita", "Mosh", "Mary"]
# We use square brackets '[]' to write lists and separate each item with a comma.

print(names)
# Prints the entire list

print(names[2])
# Prints the item of the list having index = 2.
# Indexing starts from 0.

print(names[-1])
# We can also use -1 as the value of the index.
# -1 represents the last element of the list.
# -2 represents the second last element of the list or second element from the end of the list.

names[0] = "Jon"
# Modifies the element having an index of 0.

print(names)

# We can also select a range of values.
print(names[0:3])
# This prints the elements from start index i.e. from 0 upto the end index but excluding the end index i.e. 3.
# So, this is going to print the elements at index 0, 1 and 2.
# This expression does not modify our original list.
# It prints a new list.

print(names)

# Objects in python are like real-life objects like bicycle, mobile phone, remote, etc.
# So, they have some capabilities.
# Lists are also objects just like strings.
# So, they also have some methods.

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
# Appends or add 6 at the end of the list

numbers.insert(0, -1)
# By pressing Cmd + P we can see the parameter info of the insert method.
# So, first parameter is an index which is of integer type and second parameter is an object of type 'T' i.e. it can take any type of object like boolean, number, string, etc.

numbers.remove(3)
# Removes 3 from the list

numbers.clear()
# Clears the entire list and does not take any argument.

print(numbers)
print(1 in numbers)
# Checks if 1 is present in the list or not.

print(len(numbers))
# len() is also a built-in function like print()
# It return the length of list i.e. the number of elements in a list.
# Built-in functions are highlighted as purple in pycharm.



