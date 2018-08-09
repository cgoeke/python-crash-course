# 5-2. More Conditional Tests: Have at least one True and one False result for
# each of the following:

# Tests for equality and inequality with strings
car = "Honda"

print(car == 'Honda')
print(car == "Ford")

# Tests using the lower() function
print("\nUsing lower():")
print(car.lower() == 'honda')
print(car.lower() == 'Honda')

# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
print("\nEquality:")
print(1 == 1)
print(1 == 2)

print("\nInequality:")
print(1 != 2)
print(1 != 1)

print("\nGreater than:")
print(2 > 1)
print(1 > 2)

print("\nLess than:")
print(1 < 2)
print(2 < 1)

print("\nGreater than or equal to:")
print(1 >= 1)
print(1 >= 2)

print("\nLess than or equal to:")
print(1 <= 1)
print(2 <= 1)

# Tests using the and keyword and the or keyword
print("\nAnd keyword:")
print(1 == 1 and 2 ==2)
print(1 == 1 and 1 == 2)

print("\nOr keyword")
print(1 == 1 or 1 == 2)
print( 1 == 2 or 2 == 1)

# Test whether an item is in a list
numbers = [1, 2]

print("\nIs in a list:")
print(1 in numbers)
print( 3 in numbers)

# Test whether an item is not in a list
print("\nNot in list")
print(3 not in numbers)
print(2 not in numbers)