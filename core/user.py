import hashlib
from data.user_data import UserData

class User(UserData):
  def login(self):
    user_data = None
    flag = 0
    
    while True:
      email = input("Enter email: ").strip().lower()
      password = input("Enter password: ").strip()

      data = self.get_by_email(email)
      
      if not data and flag < 3:
        print("Invalid email or password!\n")
        flag += 1
        continue
      
      if flag >= 3:
        print("You have tried to login 3 times. Please try again!\n")
        break
      
      password_hash = str(hashlib.md5(bytes(str(password).encode('utf-8'))).hexdigest())
      
      if data['password'] == password_hash:
        user_data = data
        print("Login successfully!")
        break
      
      print("Invalid email or password!")
      
    return user_data
  
  def register(self):
    user_data = None
    
    while True:
      name = input("Enter name: ").strip()
      email = input("Enter email: ").strip().lower()
      password = input("Enter password: ").strip()

      email.replace(" ", "")

      data = self.get_by_email(email)
      
      if data:
        print("Email has been registered!")
        continue
      
      password_hash = str(hashlib.md5(bytes(str(password).encode('utf-8'))).hexdigest())
      
      self.payload = {
        "name": name,
        "email": email,
        "password": password_hash
      }
      
      user_data = self.insert()
      print("Successfully registered an account!")
      break
    
    return user_data
