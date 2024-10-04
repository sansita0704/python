# We use if statements to make decisions in our program.

temperature = 25

if temperature > 30:
    # After adding colon, as we press enter the caret gets indented.
    # This means a block of statements.
    # In python, we use indentation to represent a block of code.
    # Whatever we write here will be executed only when the if statement returns a true value.

    print("It's a hot day.")
    # Here, we had a single quote in the string itself so we can't use single quotes to write the string.
    # If we write 'It's a hot day' then python will think that it is the end of the string after the word 'it'.
    # So, it will not recognize subsequent characters as the part of the string.
    # Hence, we will get an error.

    print("Drink plenty of water.")
    # To move out of this block, press shift + tab.

elif temperature > 20:
# This means the temperature is between 20 and 30 i.e. (20, 30]
    print("It's a nice day")
elif temperature > 10:
# Temperature = (10, 30]
    print("It's a bit cold")
else:
    print("It's cold.")
    # This will be executed if none of the conditions written above are true.

# Now, whatever we write here will always be executed whether the if statement is true or false.
print("Done")

# Exercise

weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == 'K':
# if unit == 'k' or unit == 'K'
    print("Weight in Lbs: " + str(weight / 0.45))
else:
    print("Weight in Kg: " + str(weight * 0.45))
