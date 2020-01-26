class UserData:

    """
    class to create new user acounts
    """

    create_acount =[]

    def __init__(self, firstName, lastName, email, username, password):

        """
        initializes the class
        """

        self.fistName = firstName
        self.lastName = lastName
        self.email = email
        self.username = username
        self.password = password

    def save_account(self):

        """
        saves the new user to create_account list
        """

        UserData.create_acount.append(self)

    #  @classmethod()
     def user_login(cls, used_name, used_password):
         """
         checks whether user exist
         """
         for user in UserData.create_acount:
             if user.username == used_name and user.password == used_password
             return user
         return False    


