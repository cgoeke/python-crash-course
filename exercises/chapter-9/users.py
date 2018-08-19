# 9-3. Users: Make a class called User  Create two attributes called first_name and last_name, and then create several other    
# attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s          # information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user. 
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

christian = User("Christian", "Goeke", "cgoeke")
christian.describe_user()
christian.greet_user()

print("\n")

amy = User("Amy", "Fernandez", "Fernanimal")
amy.describe_user()
amy.greet_user()