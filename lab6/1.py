class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self,new_password):
        self.password=new_password
    def check_password(self,password):
        return self.password == password
UserAccount1 = UserAccount('AAAA','aaa@email.com','aaa')

UserAccount1.set_password('bbb')
print(UserAccount1.check_password('bbb'))
