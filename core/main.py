import sys
from time import sleep
from core.todo import Todo
from core.user import User

class Main:
    def __init__(self):
        self.user = User()

    def run(self):
        user_data = None
        
        while True:
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            print("----------------\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                data = self.user.login()
                if not data:
                    sys.exit()
                user_data = data
                
                break
            elif choice == 2:
                self.user.register()
                continue
            elif choice == 3:
                print("Terminating program")
                sys.exit()    
            else:
                print("Invalid choice")
                
        print("----------------\n")
        print(f"Hello, {user_data['name']}. Welcome to our ToDo App!")
        print("----------------\n")
        
        print("Now loading.....")
        sleep(4)
        todo = Todo(user_data['id'])
        
        while True:
            print("\nMenu:")
            print("1. View Todo")
            print("2. Create Todo")
            print("3. Edit Todo")
            print("4. Delete Todo")
            print("5. Mark as Finished")
            print("6. Logout")
            print("----------------\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                data = todo.get_todo()
                print
            elif choice == 2:
                todo.create_todo()
                continue
            elif choice == 3:
                todo.update_todo()
                continue
            elif choice == 4:
                todo.delete_todo()
                continue
            elif choice == 5:
                todo.finish_todo()
                continue
            elif choice == 6:
                print("Terminating program")
                break
            else:
                print("Invalid choice")