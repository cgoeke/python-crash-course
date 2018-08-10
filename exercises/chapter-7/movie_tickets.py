# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.



while True:
    age = input("\nWhat is your age? \nEnter 'quit' to exit: ")
    if age == 'quit':
        break
    age = int(age)
    
    if age > 12:
        print("The ticket price is $15.00")
    elif age > 2:
        print("The ticket price is $10.00")
    else: 
        print("The ticket price is free!")
