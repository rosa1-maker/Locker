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
    






