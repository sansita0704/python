numbers = [1, 2, 3, 4, 5]
# If we print this list using print(), then it gets printed using square bracket notation.
# But if we want to print each item on a separate line, we can use for loop.

for item in numbers:
# This line starts a for loop which iterates through each element of 'numbers' list.
    print(item)
# 'in' operator when used in for loop allows us to iterate through each element of the list.
# So, in the first iteration the variable item is set to 1st element of the list.
# Then, the body of the loop gets executed.
# After that, item is set to 2nd element and the same process gets repeated until all the elements of the list are processed.

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# We can use while loop to do the same, but it will be a little bit longer than for loop.
# In for loop, we have to declare a loop variable and have to explicitly increment it by 1.
# Whereas in while loop the 'item' variable automatically gets assigned to each element of the list in every iteration.
# In for loop, we have to call len() to calculate length of the list.

integers = range(5, 10, 2)
# range() is a built-in function which is used to generate a sequence of numbers.
# It returns a range object.
# A range object is an object which can store a sequence of numbers.
# 'range(5)' - This generates a sequence of numbers starting from 0 upto the specified number.
# 'range(5, 10)' - This generates a sequence of numbers starting from 5 upto the 10 (excluding 10) i.e. numbers 5 to 9.
# If we supply a third number, it will be taken as step.
# 'range(5, 10, 2)' - This generates a sequence of numbers starting from 5 upto the 10 (excluding 10) and jumping 2 steps after each number i.e. numbers 5, 7, 9.

print(integers)
# When we print a range object, we do not see the actual numbers, but we see a range.
# This is the default representation of a range object.

for integer in integers:
    print(integer)
# We can use for loop for any object which represents a sequence of objects.

# We use range() in loops because it is not necessary to store the range object into a variable.
# We can directly use it in loops.
for number in range(5):
    print(number)