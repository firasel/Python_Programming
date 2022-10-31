class User:
    def __init__(self, name, password, phone):
        self.name = name
        self.__password = password
        self.phone = phone

    def __get_password(self):
        print(self.__password)

    def user_login(self, name, password):
        if name == self.name and password == self.__password:
            return True
        else:
            return False


ryan = User('Ryan Dal', '124365', '0123654987')
# print(ryan.__password)
print(ryan.phone)
# ryan.__get_password()
print(ryan.user_login('Ryan Dal', '124366'))
