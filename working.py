#!/usr/bin/env python3.6
import random
import string
import pyperclip
from userData import UserData
from required_data import RequiredData
import sys

sys.setrecursionlimit(10**6) 
def new_users(name_first, name_two, email_adress, user_name, pass_word):
    """
    It creates a new user
    """
    new_user = UserData(name_first, name_two, email_adress, user_name, pass_word)

    return new_user


def save_accounts(account):
    """
    It saves the new user's account
    """
    account.save_account()


def lookfor_user(used_name, used_password):
    """
    It checks if the user already exists
    """
    user_exits = UserData.user_login(used_name, used_password)

    return user_exits


def add_required(account, account_name, account_password):
    """It will add the requires data
    """
    add_required = RequiredData(account, account_name, account_password)

    return add_required


def save_required(required):
    """
     saves the created required
     """
    required.save_required()


def anypassword():
    """
    generates a random password
    """

    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    password = ''.join(random.choice(characters) for x in range(size))

    return password


def display_required():
    """
    returns the saved required data
    """
    return display_required()


def delete_required(required):
    """
    delete a required data
    """
    required.delete_required()

    


def main():
    print("\n")
    print("Welcome to Password Locker")
    print("This will store your required data and generate a password for you")

    while True:
        print("Type register to create account. If you already created one, type signin.")
        account_login = input()
        if account_login == "register":
            print("First Name:")
            firstName = input()
            print(' ')
            print("Last Name:")
            lastName = input()
            print(' ')
            print("Username:")
            username = input()
            print(' ')
            print("Email:")
            email = input()
            print(' ')
            print("To create password, type generate")
            password_choice = input()
            while True:
                if password_choice == "generate":
                    print("Password:")
                    password = input()
                    break
                elif password_choice == "generate":
                    password = anypassword()
                    print(' ')
                    break
                else:
                    print("Type 'generate")
                    break
            save_accounts(new_users(firstName, lastName, email, username, anypassword))
            print("Created successfully.")
            print(f" Username: {username}, password: {password}")
            print(' ')
            break

        elif account_login == "signin":
            print("Sign In: ")
            print("Username:")
            username = input()
            print(' ')
            print("Password:")
            password = input()
            print(' ')
            sign_in = lookfor_user(username, password)
            if sign_in == True:
                break
            print("Please sign up to access password locker.\n")

        else:
            print("Try the choices above")

    while True:
        print(f"Type create to add the required data, saved to see the saved required data or exit to stop adding required data")

        required = input()

        if required == 'create':
            print("Type platform to add:")
            plat_form = input()
            print(" ")

            print("Type in username for the platform:")
            username2 = input()

            print("To create a password, type generate ")
            pass_choice = input()
            while True:
                if pass_choice == "generate":
                    print("Password:")
                    password2 = input()
                    break
                elif pass_choice == "generate":
                    password2 = anypassword()
                    print(' ')
                    break
                else:
                    print("Type 'generate")
                    break

            save_required(add_required(plat_form, username2, password2)) 
            print(' ')
            print(f" {plat_form}: {username2}: {password2}")
            print(' ')

        elif required == 'saved':
            print("Enter your password: ")
            requiredPassword = input()
            print(' ')
            if requiredPassword == password:
                display_required()
                print("Required: ")
                for required in display_required():
                    print(
                        f"Platform => {required.platform}: Username => {required.username}: Password => {required.password}")
                    print(' ')
            else:
                print(
                    "There are no more required data saved for now. Type create to create a required data.")
                print(' ')
        elif required == 'exit':
            break

        else:
            print("Sorry, try again.")
            print(' ')


if __name__ == '__main__':
    main()
