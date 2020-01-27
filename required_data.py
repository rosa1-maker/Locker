class RequiredData:

   """
   create new data
   """

   required = []

   def _init_(self, platform, username, password):

       self.platform = platform
       self.username = username
       self.password = password

   def save_required(self):

       """
       save users objects to the users list
       """
       RequiredData.required.append(self)

       @classmethod

    def display_required(cls):

        """
        displays the required data 
        """
        return cls.required  

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
            print('/n')
            print("Last Name:")
            lastName = input()
            print('/n')
            print("Username:")
            username = input()
            print('/n')
            print ("Email:")
            email = input()
            print('/n')
            print("To create")
