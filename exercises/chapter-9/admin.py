# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.
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
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Prints Admin privileges."""
        print("Admin Privileges: ")
        for privilege in self.privileges:
            print(" " + privilege)


my_admin = Admin('Christian', 'Goeke')
my_admin.show_privileges()