"""Classes representing Admin and privileges."""
from user import User

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