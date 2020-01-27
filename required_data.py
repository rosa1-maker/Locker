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
            print("To create password, type generate a password")
            password_choice = input()
             while True:
                if pass_choice == "generate":
                    print("Password:")
                    password = input()
                    break
                elif pass_choice == "generate":
                    password = anypassword()
                    print('\n')
                    break
                else:                    
                    print("Type 'generate")
                    break
            save_accounts(new_users(firstName, lastName, emails, username, password))
            print("Created successfully.")
            print(f" Username: {username}, password: {password}.")
            print('\n')
            break

         elif account_login == "signin":
            print("Sign In:\n")
            print("Username:")
            username = input()
            print('\n')
            print("Password:")
            password = input()
            print('\n')
            sign_in = check_user(username, password)
            if sign_in == True:
                break
            print("Please sign up to access password locker.\n")

        else:
            print("Try the choices above")

    while True:
        print(f"Type create to add the required, saved to see the saved required data or exit to stop adding required data")      

        required2 = input()

        if required2 == 'create':
            print("Type platform to add:")
            plat_form = input()
            print("\n")

            print("Type in username for the platform:")
            username2 = input()

            print("To create a password, type create or to generate a password type generate")
            pass_choice = input()
             while True:
                if pass_choice == "generate":
                    print("Password:")
                    password2 = input()
                    break
                elif pass_choice == "generate":
                    password2 = anypassword()
                    print('\n')
                    break
                else:
                    print("Type 'generate")
                    break

            save_required(add_required(plat_form, username2, password2))
            print('\n')
            print(f" {plat_form}: {username2}: {password2}")
            print('\n')

            elif required2 == 'saved':
            print ("Enter your password: ")
            requiredPassword = input()
            print ("\n")        
            if requiredPassword == password:       
                display_required()
                print("Required:\n")
                for required in display_required():
                    print(f"Platform => {required.platform}: Username => {required.username}: Password => {required.password}")
                    print('\n')
            else:
                print("There are no more required data saved for now. Type create to create a required data.")
                print('\n')
        elif required2 == 'exit':
                    break
        else:
            print("Sorry, try again.")
            print('\n')


if __name__ == '__main__':
    main()
                                            
