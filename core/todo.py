from time import sleep
from data.todo_data import TodoData


class Todo(TodoData):
    def __init__(self, user_id):
        super(Todo, self).__init__()
        self.user_id = user_id
        
    def get_todo(self):
        data = self.get(self.user_id)
        
        if len(data) < 1:
            print("\nYou don't have a ToDo yet!\n")
            sleep(2)
            return False
        
        print("Register ToDo: ")
        print("-------------------------------")
        for item in data:
            status = "Unfinished" if not item['finished_at'] else "Finished"
            
            print(f"ID: {item['id']}")
            print(f"Title: {item['title']}")
            print(f"Description: {item['description']}")
            print(f"Status: {status}")
            print(f"---------------------------")
        
        sleep(5)
        input("Press enter to return to menu")
        return True
        
    def create_todo(self):
        todo_data = None
        add_todo = True
        
        while add_todo:
            title = input("Enter the ToDo title: ").strip()
            description = input("Enter ToDo description: ").strip()

            self.payload = {
                "title": title,
                "description": description,
                "user_id": self.user_id,
                "finished_at": None
            }

            todo_data = self.insert()
            print("Successfully added ToDo!")
            sleep(1)
            
            while True:
                option = input("Add another ToDo? (y/n): ").strip()
                option.replace(" ", "")
                
                if option not in ["y", "n"]:
                    print("Enter the correct choice! (y/n)")
                    continue
                
                if option == "n":
                    add_todo = False
                    
                break

        return todo_data
    
    def update_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Enter the ToDo ID: "))
            
            data = self.get(user_id=self.user_id, id=todo_id)
            
            if not data:
                print("ToDo ID not found!")
                return
            
            if self.user_id != data['user_id']:
                print("ToDo ID not found!")
                return
            
            print(f"{data['title']} - {data['description']}\n")
            title = input("Enter the title of ToDo (leave blank if you don't want to make changes): ").strip()
            description = input("Enter the description of ToDo (leave blank if you don't want to make changes): ").strip()
            
            if not title:
                title = data['title']
                
            if not description:
                description = data['description']

            self.payload = {
                "title": title,
                "description": description
            }

            todo_data = self.update(todo_id)
            print("Successfully updated the ToDo!")
            sleep(4)
            break

        return todo_data
    
    def finish_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Enter the todo ID: "))
            
            data = self.get(user_id=self.user_id, id=todo_id)
            
            if not data:
                print("Todo ID not found!")
                sleep(4)
                return None

            todo_data = self.finish(todo_id)
            print("Successfully marked ToDo as finished!")
            sleep(4)
            break

        return todo_data
    
    def delete_todo(self):
        todo_data = None

        while True:
            todo_id = int(input("Enter the todo ID: "))
            
            data = self.get(user_id=self.user_id, id=todo_id)
            
            if not data:
                print("Todo ID not found!")
                sleep(4)
                return

            self.delete(todo_id)
            
            todo_data = True
            print("Successfully deleted ToDo!")
            sleep(4)
            break

        return todo_data
