"""Provide login and signup functions for the application."""
from Utility import Utility
from User import User


class AccessManager:
    """Manage user login and account creation."""

    @staticmethod
    def Login():
        """Check the entered user ID and password."""
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")

        for user in Utility.users:
            if str(user.id) == user_id and user.password == password:
                Utility.current_user = user
                Utility.log("Logged in")
                print("Login successful.")
                return True

        Utility.log(f"Failed login attempt for User ID {user_id}")
        print("Invalid User ID or password.")
        return False

    @staticmethod
    def SignUp():
        """Create a new user account."""
        name = input("Enter your name: ")
        if not name:
            print("Name should not be empty.")
            return

        password = input("Enter your Password: ")
        if not password:
            print("Password should not be empty.")
            return

        new_user = User(Utility.Upcoming_UserId, name, password)
        Utility.users.append(new_user)
        Utility.Upcoming_UserId += 1
        Utility.current_user = new_user
        Utility.log("Signed up and logged in")
        Utility.current_user = None
        print("User created successfully. Your User ID is", new_user.id)
