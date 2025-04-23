import json

class Card:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
    
    def display_info(self):
        return f"{self.questions} - {self.answers}"
    
    def to_dict(self):
        return {"questions": self.questions, "answers": self.answers}

# Base class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"Name: {self.name}, Email: {self.email}"

# Teacher class
class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

# Student class
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

# Get input from user
x = input("What is the question? ")
y = input("What is the answer? ")

# Create a new Card object
new_card = Card(x, y)

# Display the card info
print(new_card.display_info())

# Add the card to a list
card_list = [new_card.to_dict()]

# Write to JSON file
with open("FlashCards.json", "w") as file:
    json.dump(card_list, file, indent=4)
