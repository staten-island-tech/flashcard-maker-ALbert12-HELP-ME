import json

class Teacher:
    def __init__(self, questions, answers):
        self.umm = x
        self.ummm = y
    
    def display_info(self):
        return f"{self.questions} {self.answers}"
    
    def to_dict(self):
        return {"questions": self.questions, "answers": self.answers}

x=input("what is the question?")
y=input("what is the answer?")

newTeacher = Teacher(x,y)
print (newTeacher.display_info)

newTeacher.append(newTeacher.to_dict())

with open("FlashCards.json", "w") as file:
    json.dump(newTeacher, file, indent=4)