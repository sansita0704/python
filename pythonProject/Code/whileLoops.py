# We use While Loops to repeat a block of code multiple times.
# For example, we want to print numbers from 1 to 5
# One way to do this is to print every number individually

print("1")
print("2")
print("3")
print("4")
print("5")
# But if we want to print 1 million numbers then we have to write 1 million lines.
# Instead, we can use while loop.

i = 1
while i <= 5:
    print(i)
    i += 1
# First, we define a variable i.
# Then we use while keyword and write a condition after that.
# Then we write a block of code which gets executed until the specified condition is true.
# At the end, we increment i by 1. Otherwise, it will never terminate because the value of i will remain 1 only.
# So, it will run until it runs out of memory.

i = 1
while i <= 5:
    print(i * '*')
    i += 1
# Multiplication operator is different from addition operator.
# We cannot add a string and a number.
# But we can multiply a string and a number.
# This will repeat the string based on that number.
# So, if i = 1, we will get one '*'.
# If i = 5, we will get five '*'.