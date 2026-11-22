from Utility import Utility
from User import User


class AccessManager:
    @staticmethod
    def Login():
        user_id = input("Enter User ID: ")
        password = input("Enter Password: ")

        for user in Utility.users:
            if str(user.id) == user_id and user.password == password:
                print("Login successful.")
                return True

        print("Invalid User ID or password.")
        return False

    @staticmethod
    def SignUp():
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
        print("User created successfully. Your User ID is", new_user.id)
