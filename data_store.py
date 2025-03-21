class DataStore:
    def __init__(self, filename):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return eval(file.read())  # Simple eval for demo; use JSON in production
        except FileNotFoundError:
            return {}

    def save_tasks(self, tasks):
        with open(self.filename, 'w') as file:
            file.write(str(tasks))
