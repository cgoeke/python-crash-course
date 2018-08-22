# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.
def file_reader(filenames):
    """Takes in a list of text files and prints contents to the screen."""
    for filename in filenames:
        try:
            with open(filename) as file_object:
                content = file_object.read()

        except FileNotFoundError:
            pass

        else:
            print(content)     


file_reader(['cats.txt', 'dogs.txt'])
