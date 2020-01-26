import random
import string

from userData import UserData
from required_data import RequiredData



def new_users(name_first, name_two, email_adress, user_name, pass_word):

    """
    It creates a new user
    """
    new_user = UserData(name_first, name_two, email_adress, user_name, pass_word)

    return new_user

def save_accounts(account)    :
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
    add_required =RequiredData(account, account_name, account_password)

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
    password =''.join(random.choice(characters) for x in range(size))

    return password

def display_required():
    """
    returns the saved required data
    """
    return RequiredData.display_required()

    











