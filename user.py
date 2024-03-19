#@User information class 
class User:
    #@Constructor method to initialize a User object with given name and user ID.
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"User({self.name}, {self.user_id})"

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["user_id"])