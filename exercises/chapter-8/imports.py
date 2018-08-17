# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
import cars
from cars import make_car
from cars import make_car as mc
import cars as c
from cars import *

my_car = cars.make_car('lamborghini', 'countach', color = 'red', year = 1980 )
print("\n")
print(my_car)

my_car = cars.make_car('lamborghini', 'countach', color = 'red', year = 1980 )
print("\n")
print(my_car)

my_car = mc('lamborghini', 'countach', color = 'red', year = 1980 )
print("\n")
print(my_car)

my_car = c.make_car('lamborghini', 'countach', color = 'red', year = 1980 )
print("\n")
print(my_car)

my_car = make_car('lamborghini', 'countach', color = 'red', year = 1980 )
print("\n")
print(my_car)