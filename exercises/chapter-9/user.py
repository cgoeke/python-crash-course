"""A class that defines a user."""
class User():
    """Defines a User class."""
    def __init__(self, first_name, last_name, user_name):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def describe_user(self):
        """Prints summary of the user profile."""
        print(self.user_name + "'s profile:")
        print(" First Name: " + self.first_name)
        print(" Last Name: " + self.last_name)

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print("\nHello " + self.user_name + "!")