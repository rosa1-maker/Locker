class RequiredData:

   """
   create new data
   """

   required = [] 

   def __init__(self, platform, username, password):
       """
            creates an initailization for the new data
       """
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
        return cls.display_required  


                                            
