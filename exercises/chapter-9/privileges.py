# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.
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


class Admin(User):
    """Defines Admin class."""

    def __init__(self, first_name, last_name, user_name='Admin'):
        """Initializes Admin."""
        super().__init__(first_name, last_name, user_name)
        self.privileges = Privileges()


class Privileges():
    """Privileges class."""

    def __init__(self, privileges=[]):
        """Initialize Privileges class."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints Admin privileges."""
        print("Admin Privileges: ")
        for privilege in self.privileges:
            print(" " + privilege)


my_admin = Admin('Christian', 'Goeke')
my_admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
my_admin.privileges.show_privileges()