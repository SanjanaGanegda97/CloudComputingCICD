class Patient:
    def __init__(self, id, name, age, medical_history):
        self.id = id
        self.name = name
        self.age = age
        self.medical_history = medical_history

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "medical_history": self.medical_history,
        }
