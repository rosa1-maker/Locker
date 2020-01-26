class RequiredData:

   """
   create new data
   """

   required = []

   def _init_(self, platform, username, password):

       self.platform = platform
       self.username = username
       self.password = password

#    def save_required(self):

#        """
#        save users objects to the users list
#        """

#        RequiredData.required.append(self)

#     @classmethod

#     def display_required(cls):

#         """
#         display the required
#         """
#         return cls.required   
