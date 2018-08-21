# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.
while True:
    print('Enter "q" to quit')
    name = input('Please enter your name: ')

    if name == 'q':
        break
    else:
        greeting = 'Hello, ' + name + '!'
        print(greeting)
    
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(name + '\n')