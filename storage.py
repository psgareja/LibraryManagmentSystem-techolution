import json
import os

#@Data base class
class Storage:
    def __init__(self, filename):
        self.filename = filename

    #@save_data(self, data): Saves data to the JSON file.
    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
            
    #@load_data(self): Loads data from the JSON file.
    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)
