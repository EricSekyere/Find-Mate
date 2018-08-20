import bcrypt
import json
class User(): 
    salt = bcrypt.gensalt()
    def __init__(self, fn, ln, email, pwd):
        self.fn = fn
        self.ln = ln
        self.email = email
        self.pwd = self.set_pwd(str(pwd).encode('utf-8'))

    def set_pwd(self, pwd):
        hashed = bcrypt.hashpw(pwd, self.salt)
        return hashed

    def jsonify_data(self, parameter_list):
        pass


class Password_Validator():
    ''' 
    def __init__(self, password):
        self.password = self.check_pwd(password)
    '''
    def check_pwd(self, pwd):
        return bcrypt.checkpw(pwd.encode('utf-8'), pwd)