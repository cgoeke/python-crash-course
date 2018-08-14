# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(size='large', message='I love Python'):
    """makes a shirt provided size and message."""
    print("You requested a " + size + " shirt with the message: " + message + ".")

make_shirt()
make_shirt(size='medium')

make_shirt(size='xl', message='My shirt is extra large')