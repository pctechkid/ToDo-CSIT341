from datetime import datetime

todo_data = [
    {'title': 'Project Presentation', 'description': 'Final Project Presentation of CSIT341', 'user_id': 1, 'finished_at': None, 'id': 1}
]

class TodoData:
    def __init__(self):
        self.todo_data = todo_data
        self.payload = {}

    def validate(self, payload):
        if 'title' not in payload or not payload['title']:
            raise Exception("You should fill title")

        if 'description' not in payload or not payload['description']:
            raise Exception("You should fill description")

    def clear(self):
        self.payload = {}

    def get(self, user_id=None, id=None):
        if not id:
            todos = []
            
            if len(self.todo_data) < 1:
                return todos
            
            for item in self.todo_data:
                if item['user_id'] == user_id:
                    todos.append(item)
                continue
                
            return todos

        value = None
        for item in self.todo_data:
            if item['id'] == id and user_id == item['user_id']:
                value = item
                break

        return value

    def insert(self):
        self.validate(self.payload)

        length = len(self.todo_data)
        self.payload['id'] = (length + 1)

        self.todo_data.append(self.payload)
        data = self.payload.copy()

        self.clear()
        return data

    def update(self, id):
        self.validate(self.payload)

        for item in self.todo_data:
            if item['id'] == id:
                item.update(self.payload)
                break

        self.clear()
        
    def finish(self, id):
        for item in self.todo_data:
            if item['id'] == id:
                item['finished_at'] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                break

        return True

    def delete(self, id):
        index = 0

        for idx, item in enumerate(self.todo_data):
            if item['id'] == id:
                index = idx
                break

        self.todo_data.pop(index)
        self.clear()
