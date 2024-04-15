from users.admin import Admin
from users.users import User
from product import Product
from users.admincredentials import ADMIN_USERNAME, ADMIN_PASSWORD
from users.usercredentials import USER1_USERNAME, USER1_PASSWORD
from interface import Interface


def welcomepage():
    print("Welcome to Karra's Marketplace")
    print("Login")
    return input("Admin A or User U: ")


def credentials():
    return input("User ID: "), input("Password: ")


def main():
    user_mode = welcomepage()
    username, password = credentials()
    the_user = None
    if user_mode == "A":
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            the_user = Admin(username, password)
            print("Login Successful")
            inter = Interface()
            inter.admin_interface(username)
            inter.admin = the_user
        else:
            print("Incorrect Username or Password")
    elif user_mode == "U":
        if username == USER1_USERNAME and password == USER1_PASSWORD:
            the_user = User(username, password)
            print("Login Successful")
            inter = Interface()
            inter.user_interface(the_user, username)
            inter.users.append(the_user)
        else:
            print("Incorrect Username or Password")
    main()


if __name__ == "__main__":
    main()
